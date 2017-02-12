import sys
import requests
#import pycountry

def tracking(str):
    tracking_number= str
    if len(tracking_number) != 13:
        result = ' the ',tracking_number,' dose not seem like an ELTA tracking number...'
    else:
        r = requests.post('http://www.elta-courier.gr/track.php', data = { 'number': tracking_number})
        result = r.json()
        #Country_origin = pycountry.countries.lookup(tracking_number[-2:])
        #print ('Origin is: '+ Country_origin.name)
    return (result)
