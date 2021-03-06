import requests
import json

url = 'http://qainterview.cogniance.com/candidates'


class ListCandidate:
    def get(self):
        res_cands = requests.get(url)
        return res_cands

class Candidate:
    def get(self, cid):
        res_cand = requests.get(url+r'/'+str(cid))
        return res_cand

    def post(self, name, position):
        data={'name': name, 
               'position': position}
        res_new_cand = requests.post(url, 
                                     headers={'content-type': 'application/json'},
									 
                                     data=json.dumps(data) )
        return res_new_cand

    def delete(self, del_cand):
        del_candid = requests.delete(url+r'/'+str(del_cand))
        return del_candid
