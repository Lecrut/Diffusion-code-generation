def is_identical(obj1, obj2):
    return obj1 == obj2

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1, 2, 4]
    
    results = {
        (list1, list2): is_identical(list1, list2),
        (list1, list3): is_identical(list1, list3)
    }
    
    for (obj1, obj2), result in results.items():
        print(f"{obj1} and {obj2} are identical: {result}")