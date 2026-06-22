def middle_value(lst):
    if not lst:
        return None
    n = len(lst)
    if n % 2 == 1:
        return lst[n // 2]
    else:
        return lst[n // 2 - 1]

if __name__ == '__main__':
    arr1 = [10, 20, 30]
    arr2 = [10, 20, 30, 40]
    arr3 = [1]
    arr4 = [10, 20]
    
    print(middle_value(arr1))
    print(middle_value(arr2))
    print(middle_value(arr3))
    print(middle_value(arr4))