# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import weakref

from wechatpy.client.base import BaseWeChatClient
from . import api


class WeChatClient(BaseWeChatClient):

    API_BASE_URL = 'https://qyapi.weixin.qq.com/cgi-bin/'

    def __init__(self, corp_id, secret, access_token=None):
        self.corp_id = corp_id
        self.secret = secret
        self._access_token = access_token
        self.expires_at = None

        weak_self = weakref.proxy(self)
        # APIs
        self.user = api.WeChatUser(weak_self)
        self.department = api.WeChatDepartment(weak_self)
        self.menu = api.WeChatMenu(weak_self)
        self.message = api.WeChatMessage(weak_self)
        self.tag = api.WeChatTag(weak_self)
        self.media = api.WeChatMedia(weak_self)
        self.misc = api.WeChatMisc(weak_self)

    def fetch_access_token(self):
        """ Fetch access token"""
        return self._fetch_access_token(
            url='https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={
                'corpid': self.corp_id,
                'corpsecret': self.secret
            }
        )
