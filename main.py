import requests
import time
url = 'https://xk.xidian.edu.cn/xsxk/elective/clazz/add'
headers ={
    #用户信息也是改变的 #每次AU都需要提前几分钟改变一下别的不用变
    "Authorization":"",
    "User-Agent": "",
}
#课程信息
data = {
    "clazzType": "",
    "clazzId": "",
    #改变的东西
    "secretVal": "",
}
n = 0
while(1):
    n+=1
    response = requests.post(url,headers=headers,data=data)
    print(n,response.json())
    if(response.json()["code"]==200):
        response.close
        break
    else:
        time.sleep(0.001)
print("over") 



