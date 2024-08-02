import numpy as np
class InterConfMedia:
    "calcula intervalo de confiança para média"
    
    def __init__(self, amostra=[]):
        #self.s = s
        self.v_media = 0
        self.v_dvp = 0
        self.amostra = amostra
        self.e = 0
        self.c = 0

    def dvp(self):
        self.v_dvp = np.std(self.amostra)
        return self.v_dvp
        
    def media(self):
        self.v_media = np.mean(self.amostra)
        return self.v_media

    def margemErro(self, zc=1.96):
        s = self.v_dvp
        n = len(self.amostra)
        e = zc*(s/(n**0.5))
        self.e = e
        return self.e

    def interConf(self):
        extremo_equerdo = self.v_media - self.e
        extremo_direito = self.v_media + self.e
        print(extremo_equerdo, self.v_media, extremo_direito)

    def tamAmostra(self, zc=0, s=0, e=0):
        n = (zc*s)/e
        return n*n
        
        
