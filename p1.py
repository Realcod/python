import copy

list=["apple","banana","brinjal",1+4j]
list1=["second fruit","third fruit"]
#what is list
print(list)

#what is slicing in list
print(list[0:3])

#what is append
list.append("yash")
print(list)

#what is insert
list.insert(1,"monika")
print(list)

#what is extend
list.extend(list1)
print(list)

#what is repeation factor
new_list=list1[0]*3
print(new_list)

#shallow copy

#new_list=list
#list[0]="updated one"
#new_list[1]="updated_two"
#print(new_list)
#print(list)

#deep copy
new_listt=copy.copy(list)
print(new_listt)
list[0]="updated one"
new_listt[1]="updated one"
print(new_listt)
print(list)

#sorted
my_list = [3, 1, 4, 1, 5, 9]
my_list.sort()
print(my_list)

#index
print(list.index("updated one"))

#length
print(len(list))

#count
print(my_list.count(1))

#remove
my_list.remove(4)
print(my_list)

#delete
del new_listt
#print(new_listt)

#pop
print(list)
list.pop(0)
print(list)

#clear
print(my_list)
my_list.clear()
print(my_list)

#list comprehension
numbers=[2,4,6,8,10]
ans=[]
ans = [x**2 for x in numbers]
print(ans)