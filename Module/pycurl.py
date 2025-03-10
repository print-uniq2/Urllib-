# */* CODED BY : ARAFAT AHAMMED ! */*
import requests
from io import BytesIO
class Curl:
    def __init__(self):
        self.url = None
        self.writedata = None
        self.ssl_verifypeer = True
        self.ssl_verifyhost = True
        self.cainfo = None
        self.data = None
        self.timeout = None
        self.connecttimeout = None
        self.headers = {}
    def setopt(self, option, value):
        if option == "URL":
            self.url = value
            print(self.url)
        elif option == "WRITEDATA":
            self.writedata = value
        elif option == "SSL_VERIFYPEER":
            self.ssl_verifypeer = value
        elif option == "SSL_VERIFYHOST":
            self.ssl_verifyhost = value
        elif option == "CAINFO":
            self.cainfo = value
        elif option == "TIMEOUT":
            self.timeout = value
        elif option == "CONNECTTIMEOUT":
            self.connecttimeout = value
        elif option == "HTTPHEADER":
            self.headers = {header.split(': ')[0]: header.split(': ')[1] for header in value}
            print(self.headers)
            self.headers.update(dict(h.split(": ", 1) for h in value))
        else:
            raise ValueError(f"Unknown option: {option}")
    def perform(self):
        if not self.url:
            raise ValueError("URL not set")
        verify = self.ssl_verifypeer
        if self.ssl_verifyhost and self.cainfo:
            verify = self.cainfo
        try:
            print(self.url,self.headers)
            response = requests.get(self.url, 
                                    timeout=(self.connecttimeout, self.timeout), 
                                    headers=self.headers, 
                                    verify=verify)
            if self.writedata:
                if isinstance(self.writedata, BytesIO):
                    self.writedata.write(response.content)
                else:
                    self.writedata.write(response.text)
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
    def close(self):
        pass
    URL = "URL"
    WRITEDATA = "WRITEDATA"
    CAINFO = "CAINFO"

URL = "URL"
WRITEDATA = "WRITEDATA"
SSL_VERIFYPEER = "SSL_VERIFYPEER"
SSL_VERIFYHOST = "SSL_VERIFYHOST"
CAINFO = "CAINFO"
TIMEOUT = "TIMEOUT"
CONNECTTIMEOUT = "CONNECTTIMEOUT"
HTTPHEADER = "HTTPHEADER"
