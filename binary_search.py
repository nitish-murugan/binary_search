def formula(low,high):
    return (low+int(((high - low)/2)))
lst = [2,5,8,12,16,23,38,56,72,91].sort()
key = int(input("Enter the key element => "))
count = 0
flag = 0
low = 0
high = len(lst)-1
mid = formula(low,high)
while(count<len(lst)):
    if(lst[mid] < key):
        new_lst = lst[mid+1:]
        low = mid+1
        high = len(lst)-1
        mid = formula(low,high)
    elif(lst[mid] > key):
        low = low
        high = mid-1
        mid = formula(low,high)
    else:
        flag = 1
        print("Key found in the index: ",mid)
        break
    count = count + 1
if(flag == 0):
    print("Element not found")
