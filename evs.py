import requests
import datetime
''' extracting date time for start and end time data -> to capture limited data'''
time=(datetime.datetime.now()-datetime.timedelta(seconds=2)).strftime('%s')
newtime_two= (datetime.datetime.now() - datetime.timedelta(minutes=60)).strftime('%s')
############################################
'''----------------Girls' hostel AB wing 0th floor------------'''
gh_0_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/a2095480-eed6-584e-b5e4-d7199eee9ac3?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")
x0=gh_0_ab.content.split(',')[-1].split('\r')[0]
y0=gh_0_ab.text.split(',')[-20].split('\r')[0]#give last 10 min consumption
print "gh-0-ab starts:"
print int(float(y0))
integer0=int(float(x0))
#printing instant value in integer
print integer0
print "gh-0-ab end\n"
'''xxxxxxxxxxx Girls' hostel AB wing 0th floor ends xxxxxxxxxxxxxxxxxxx'''
#########################################
'''----------------Girls' hostel AB wing 1st floor------------'''
gh_1_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/b7c99e66-e3be-596a-baf9-47b01f9e21f9?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")
x1=gh_1_ab.content.split(',')[-1].split('\r')[0]
y1=gh_1_ab.text.split(',')[-20].split('\r')[0]
print "gh-1-ab starts:"
print int(float(y1))
integer1=int(float(x1))
#printing instant value in integer
print integer1
print "gh-1-ab end\n"
'''xxxxxxxxxxx Girls' hostel AB wing 1st floor ends xxxxxxxxxxxxxxxxxxx'''
###############################################3
'''----------------Girls' hostel AB wing 2nd floor------------'''
gh_2_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/d232a8a7-00f0-5260-95ff-5705899b2db4?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")
x2=gh_2_ab.content.split(',')[-1].split('\r')[0]
y2=gh_2_ab.text.split(',')[-20].split('\r')[0]
print "gh-2-ab starts:"
print int(float(y2))
integer2=int(float(x2))
#printing instant value in integer
print integer2
print "gh-2-ab end\n"
'''xxxxxxxxxxx Girls' hostel AB wing 2nd floor ends xxxxxxxxxxxxxxxxxxx'''
###################################################
'''----------------Girls' hostel AB wing 3rd floor------------'''
gh_3_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/c01563d5-e52e-5fcb-bd01-4fbe247ee2d4?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")
x3=gh_3_ab.content.split(',')[-1].split('\r')[0]
y3=gh_3_ab.text.split(',')[-20].split('\r')[0]
print "gh-3-ab starts:"
print int(float(y3))
integer3=int(float(x3))
#printing instant value in integer
print integer3
print "gh-2-ab end\n"
'''xxxxxxxxxxx Girls' hostel AB wing 3rd floor ends xxxxxxxxxxxxxxxxxxx'''
####################################################3
'''----------------Girls' hostel AB wing 4th floor------------'''
gh_4_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/945e47fa-2e48-5b07-8771-6c84751a269c?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")
x4=gh_4_ab.content.split(',')[-1].split('\r')[0]
y4=gh_4_ab.text.split(',')[-20].split('\r')[0]
print "gh-4-ab starts:"
print int(float(y4))
integer4=int(float(x4))
#printing instant value in integer
print integer4
print "gh-4-ab end\n"
'''xxxxxxxxxxx Girls' hostel AB wing 4th floor ends xxxxxxxxxxxxxxxxxxx'''
###################################################################################

'''----------------Girls' hostel BC wing 0th floor------------'''
gh_0_bc=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/5303e59f-33eb-57ea-a025-f85afce3316c?starttime=1428577140000&endtime=1428663540000&format=csv&tags=&timefmt=iso8601&"+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")
x0_bc=gh_0_bc.content.split(',')[-1].split('\r')[0]
y0_bc=gh_0_bc.text.split(',')[-20].split('\r')[0]#give last 10 min consumption
print "gh-0-bc starts:"
print int(float(y0_bc))
integer0_bc=int(float(x0_bc))
#printing instant value in integer
print integer0_bc
print "gh-0-bc end\n"
'''xxxxxxxxxxx Girls' hostel BC wing 0th floor ends xxxxxxxxxxxxxxxxxxx'''
#########################################

'''----------------Girls' hostel BC wing 1st floor------------'''
gh_1_bc=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/82af7ba3-db7d-518a-97b6-eae47508d2d5?starttime=1428577140000&endtime=1428663540000&format=csv&tags=&timefmt=iso8601&"+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")
x1_bc=gh_1_bc.content.split(',')[-1].split('\r')[0]
y1_bc=gh_1_bc.text.split(',')[-20].split('\r')[0]
print "gh-1-bc starts:"
print int(float(y1_bc))
integer1_bc=int(float(x1_bc))
#printing instant value in integer
print integer1_bc
print "gh-1-bc end\n"
'''xxxxxxxxxxx Girls' hostel BC wing 1st floor ends xxxxxxxxxxxxxxxxxxx'''
################################################

'''----------------Girls' hostel BC wing 2nd floor------------'''
gh_2_bc=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/376413c8-0dd0-5191-a291-091636b45a01?starttime=1428577140000&endtime=1428663540000&format=csv&tags=&timefmt=iso8601&"+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")
x2_bc=gh_2_bc.content.split(',')[-1].split('\r')[0]
y2_bc=gh_2_bc.text.split(',')[-20].split('\r')[0]
print "gh-2-bc starts:"
print int(float(y2_bc))
integer2_bc=int(float(x2_bc))
#printing instant value in integer
print integer2_bc
print "gh-2-bc end\n"
'''xxxxxxxxxxx Girls' hostel BC wing 2nd floor ends xxxxxxxxxxxxxxxxxxx'''
####################################################
'''----------------Girls' hostel BC wing 3rd floor------------'''
gh_3_bc=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/afb6540a-45e6-52ab-95c1-6f8e019dc85b?starttime=1428577140000&endtime=1428663540000&format=csv&tags=&timefmt=iso8601&"+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")
x3_bc=gh_3_bc.content.split(',')[-1].split('\r')[0]
y3_bc=gh_3_bc.text.split(',')[-20].split('\r')[0]
print "gh-3-bc starts:"
print int(float(y3_bc))
integer3_bc=int(float(x3_bc))
#printing instant value in integer
print integer3_bc
print "gh-2-bc end\n"
'''xxxxxxxxxxx Girls' hostel BC wing 3rd floor ends xxxxxxxxxxxxxxxxxxx'''
####################################################

'''----------------Girls' hostel BC wing 4th floor------------'''
gh_4_bc=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/6f96f660-5745-5467-b9b2-2a9ce4ce6b34?starttime=1428577140000&endtime=1428663540000&format=csv&tags=&timefmt=iso8601&"+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")
x4_bc=gh_4_bc.content.split(',')[-1].split('\r')[0]
y4_bc=gh_4_bc.text.split(',')[-20].split('\r')[0]
print "gh-4-bc-starts:"
print int(float(y4_bc))
integer4_bc=int(float(x4_bc))
#printing instant value in integer
print integer4_bc
print "gh-4-bc end\n"
'''xxxxxxxxxxx Girls' hostel BC wing 4th floor ends xxxxxxxxxxxxxxxxxxx'''
###################################################################################





















