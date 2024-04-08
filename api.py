import requests
from flask import *

app = Flask(__name__)

@app.route( '/' ,methods=['GET'])
           
def check():
	number = str(request.args.get('num'))
	token = str(request.args.get('token'))

	url = f'https://web.vodafone.com.eg/services/dxl/usagemng/usage?relatedParty.id={number}&@type=ConsumptionDetails&usageSpecification.id=National&$.type[0]=Voice&$.type[1]=VideoCall'

	hd = {
'Host': 'web.vodafone.com.eg',
'Connection': 'keep-alive',
'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
'msisdn': number,
'Accept-Language': 'AR',
'sec-ch-ua-mobile': '?1',
'Authorization': f'Bearer {token}',
'Content-Type': 'application/json',
'Accept': 'application/json',
'clientId': 'WebsiteConsumer',
'sec-ch-ua-platform': '"Android"',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': 'https://web.vodafone.com.eg/spa/call-details'
	}

	r = requests.get(url,headers=hd).text
	
	return r
	
if __name__ ==  '__main__' :
	app.run(host= '0.0.0.0' , port=8080)