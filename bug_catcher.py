from urllib.request import  urlopen
t1 = urlopen("http://csssr.github.io/qa-engineer/").read().decode('utf-8')
s=str(t1)
n1=s.count('bug')
print(n1, 'bugs found')
input()




