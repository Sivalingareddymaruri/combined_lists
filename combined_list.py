even_num=[2,4,6,8]
odd_num=[1,3,5,7]
combined_array=[]
for x in range(len(even_num)):
    combined_array.append(even_num[x])
    combined_array.append(odd_num[x])      
print(combined_array)