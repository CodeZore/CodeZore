import math


def MergeSort(left, right):
    l_size = len(left)
    r_size = len(right)
    l_index = 0
    r_index = 0
    newArray = []
    while l_index < l_size and r_index < r_size:
        if left[l_index] < right[r_index]:
            newArray.append(left[l_index])
            l_index += 1
        else:
            newArray.append(right[r_index])
            r_index += 1

    while l_index < l_size:
        newArray.append(left[l_index])
        l_index += 1

    while r_index < r_size:
        newArray.append(right[r_index])
        r_index += 1

    return newArray


def Merge(sArray):
    if len(sArray) < 2:
        return sArray
    size = len(sArray)
    middle = math.floor(size / 2)
    left = sArray[0:middle]
    right = sArray[middle:size]
    return MergeSort(Merge(left), Merge(right))


if __name__ == '__main__':
    s = [1, 2, 33, 21, 13, 15, 43, 23]
    n = Merge(s)

    print(s)
    print(n)
