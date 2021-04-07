import sys
import hashlib
import collections

BUF_SIZE = 65536
HASH_SIZE = 5
file1 = hashlib.sha256()
file2 = hashlib.sha256()

hash_list_1 = []
hash_list_2 = []

def common_data(list1, list2): 
    result = False
    for i, x in enumerate(list1): 
        for j, y in enumerate(list2): 
            if x[-HASH_SIZE:] == y[-HASH_SIZE:]: 
                print("real:" + x)
                print("fake:" + y)
                print('i:{} j:{}'.format(i, j))
                return True

while True:
    wrote = False
    with open('confession_real.txt') as f:
        chars = f.read()

    f= open('confession_real.txt', 'w')
    for char in chars:
        if char == '\n' and wrote == False:
            wrote = True
            char = ' ' + char
        f.write(char)

    with open("confession_real.txt", 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            file1.update(data)
    
    hash_list_1.append(file1.hexdigest())

    wrote = False
    with open('confession_fake.txt') as f:
        chars = f.read()

    f= open('confession_fake.txt', 'w')
    for char in chars:
        if char == '\n' and wrote == False:
            wrote = True
            char = ' ' + char
        f.write(char)

    with open("confession_fake.txt", 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            file2.update(data)
    
    hash_list_2.append(file2.hexdigest())

    if common_data(hash_list_1, hash_list_2):
        break



                  

# for i in range(len(hash_list_1)): 
#     print(hash_list_1[i])

# print 
# for i in range(len(hash_list_2)): 
#     print(hash_list_2[i])
