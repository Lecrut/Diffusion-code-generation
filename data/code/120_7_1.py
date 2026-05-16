def is_identical(obj1, obj2):
    return obj1 == obj2
if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1, 2, 4]
    result1 = is_identical(list1, list2)
    result2 = is_identical(list1, list3)
    print(f"list1 is identical to list2: {result1}")
    print(f"list1 is identical to list3: {result2}")