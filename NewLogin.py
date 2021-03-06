#!/usr/bin/python
#_*_coding:utf-8 _*_
#author: xwjr.com

import cgi
import urllib,urllib2
import json
import sys
import simplejson


def gettoken(corpid,corpsecret):
    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
    #print  gettoken_url
    try:
        token_file = urllib2.urlopen(gettoken_url)
    except urllib2.HTTPError as e:
        print e.code
        print e.read().decode("utf8")
        sys.exit()
    token_data = token_file.read().decode('utf-8')
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    return token
 
 
 
def senddata(access_token,TYPE,toinfo,subject,content):
    #print TYPE 
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
    send_values = {
        TYPE:toinfo,    #企业号中的用户帐号，在zabbix用户Media中配置，如果配置不正常，将按部门发送。
        "msgtype":"text", #消息类型。
        "agentid":"17",    #企业号中的应用id。
        "text":{
            "content":subject + '\n' + content
           },
        "safe":"0"
        }
#    send_data = json.dumps(send_values, ensure_ascii=False).encode('utf-8')
    send_data = simplejson.dumps(send_values, ensure_ascii=False).encode('utf-8')
    send_request = urllib2.Request(send_url, send_data)
    response = json.loads(urllib2.urlopen(send_request).read())
    #print str(response)
    return (response)
 
 
if __name__ == '__main__':

    totag = "14"
    USER = str(sys.argv[1])
    TIME = str(sys.argv[2]) 
    content = "登陆用户:" + USER + '\n' + "时间:" + TIME
    subject = "希望金融小分队跳板机登陆提醒"
    TYPE = "totag"
    corpid =  '****************'
    corpsecret = '**********************'
    accesstoken = gettoken(corpid,corpsecret)
    senddata(accesstoken,TYPE,totag,subject,content)
