def is_identical(obj1, obj2):
    return obj1 == obj2
if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1, 2, 4]
    print(f"Is list1 identical to list2? {is_identical(list1, list2)}")
    print(f"Is list1 identical to list3? {is_identical(list1, list3)}")