import requests,sys,warnings

warnings.filterwarnings("ignore")

session=requests.session()
#print("first")
#res=session.get("https://www.digikala.com/",proxies={'https':'http://127.0.0.1:8080/'},verify=False)
number=str(input("write your number: "))
print("[-] will sending OTP...")
data={"backUrl":"/","username":number,"otp_call":False,"force_send_otp":True}
res=session.post('https://api.digikala.com/v1/user/authenticate/',json=data,proxies={'https':'http://127.0.0.1:8080/'},verify=False)

if res.json()['status'] != 200:
    sys.exit(0)

print("[+] send !")
otp=str(input("Write OTP: "))
data={"backUrl":"/","type":"otp","username":"09130523009","code":otp}
res=session.post('https://api.digikala.com/v1/user/authenticate/',json=data,proxies={'https':'http://127.0.0.1:8080/'},verify=False)

if res.json()['status'] != 200:
    print("[!] OPPS...")
    sys.exit(0)

res=session.post('https://api.digikala.com/v1/digipay/balance/',proxies={'https':'http://127.0.0.1:8080/'},verify=False)
if res.json()['status'] != 200:
    print("[!] OPPS...")
    sys.exit(0)
print("Success!!!! :)")
print(res.json()['data']['wallet']['credit'])