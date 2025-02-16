# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 14:25:19 2022

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class SentimentFinancialData(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        self.URL_SENTIMENT_DATA = 'https://eodhistoricaldata.com/api/sentiments'
        super().__init__(api_key, timeout)
        
    def get_sentiment(self, **query_params):
        """
        Retrieve sentimental data calculated from the EOD historical data API 
        aggregated by day. Stocks, ETFs, Forex, and Cryptocurrencies are supported.
        You can retrieve several instruments separated by commas.

        Parameters
        ----------
        **query_params : dict
            

        Returns
        -------
        list
            sentiment score for the instrument(s).

        """
        self.endpoint = self.URL_SENTIMENT_DATA
        return super().handle_request(self.endpoint, query_params)