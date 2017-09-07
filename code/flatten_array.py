# author: Omar Sinan
# date: 07/09/2017
# description: Flatten an array - https://discuss.codecademy.com/t/challenge-flatten-an-array/218659

def flattenArray(arr):
    temparr = []
    for i in arr:
        if type(i) is list:
            temparr.extend(flattenArray(i))
        else:
            temparr.append(i)
    return temparr

# print flattenArray([1, 2, [3, [4, 5]], 6])
