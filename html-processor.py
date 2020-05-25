import re

#συνάρτηση για &amp &gt &lt &nbsp
def cb(m): 
  if (m.group(0)=='&amp;'):
    return '&'
  elif (m.group(0)=='&gt;'):
    return '>'
  elif (m.group(0)=='&lt;'):
    return '<'
  else:
    return ' '	

#ερώτημα 1
rexp1 = re.compile('<title>(.+?)</title>')	

#ερώτημα 2 
rexp2 = re.compile('<!--.*?-->',re.DOTALL)  

#ερώτημα 3
rexp3 = re.compile(r'<(s(?:cript|tyle)).*?>.*?</\1>',re.DOTALL) 

#ερώτημα 4 
rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL) 

#ερώτημα 5
rexp51 = re.compile(r'<.+?>|</.+?>',re.DOTALL) 

rexp52 = re.compile(r'<.+?/>',re.DOTALL) 

#ερώτημα 6 
rexp6 = re.compile(r'&(amp|gt|lt|nbsp);') 

#ερώτημα 7
rexp7 = re.compile(r'\s+') 

#διάβασμα αρχείου
with open('testpage.txt','r') as fp:

  keimeno = fp.read() 

  m = rexp1.search(keimeno) 
  
  print(m.group(1))	

  keimeno = rexp2.sub(' ',keimeno) 

  keimeno = rexp3.sub(' ',keimeno)

  for m in rexp4.finditer(keimeno): 
    print('{}    {}'.format(m.group(1),m.group(2))) 

  keimeno = rexp51.sub(' ',keimeno)
 
  keimeno = rexp52.sub(' ',keimeno) 

  keimeno = rexp6.sub(cb,keimeno) 

  keimeno = rexp7.sub(' ',keimeno) 

  print(keimeno)
