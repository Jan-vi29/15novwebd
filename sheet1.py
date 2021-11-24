# 2

a=5**9 #exponential
print(a)

a=3//2 # floor division 
print(a)

a=7//3 #floor division
print(a)

a=7/3 #normal division
print(a)

print(6==6) # checking

a=20
a+=30
a%=3
print(a)  #(20,20+30,50%3,2)

print(True*False)
print(True & False)
print(True and False)
print((6>3)and (7<4) or (18==3) and (9>3)) #false or false
print(True is False)

# print(False in 'False')                                   

print((True ==False) or (False > True)) and (False <=True)

# 3

s1="Nice to have it"
s2="here"
s1+=s2
print(s1)

#4

a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])



# 5

a[0]=s1
a.append(s2)
print(a)

# 6

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]

for i in numbers:
    if(i<=237)and(i%2==0):
        print(i)

#7

color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

print(color_list_1 - color_list_2)


#8

s = input("Enter the string: ")
l = list(range(65,91))           #storing ascii values of A to Z
for i in s.upper():              #changing string to upper
    if ord(i) in l:              #if ordinate of a character is found in the list l
        l.remove(ord(i))         #removing that element

if len(l) == 0:                  
    print(f"{s} is a Pangram.")
else:                            
    print(f"{s} is not a Pangram.")
#s=input('enter a string:')
#for i in range(ord('a'),ord('z')):
#  if i not in s:
        #print('not a pangram')
#  else:

        #print('pangram')


#9

n=input('num:')
a=int(n)
b = a*10 + a
c = a*100 + a*10 + a
print(a+b+c)

#10



#11

a=input('enter sequence of words:').split(',') #separating them with a ','
a.sort()                                       #sorting in alphabetic order
print(a)


#12

d={'student': ['rahul','kishore','vidhya','raakhi'],'Marks':[57,87,67,79]}
mx = max(d['Marks'])
i = d['Marks'].index(mx)                    
print(d['student'][i])

#alt
#for i in d['Marks']:
#   if d['Marks'][i] == max(d['Marks']):
#        print(d['student'][i])    



#13

str=(input("enter the sentence"))
l=0
d=0
for i in str:
    if(i.isalpha()):
        l+=1
    if(i.isdigit()):
        d+=1
print(l,d)


#14
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'], 'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'], 'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
sub = input('enter the subject:')
newData = {'Name' : [], 'Subject' : [], 'Ratings' : []}
for i in range(len(d['Name'])):
    s = d['Subject'][i] 
    if s == sub:
        newData['Name'].append(d['Name'][i])
        newData['Subject'].append(d['Subject'][i])
        newData['Ratings'].append(d['Ratings'][i])
print(newData)


#15

#16


