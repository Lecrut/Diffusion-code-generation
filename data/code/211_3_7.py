def set_operations():
    set1 = {'apple', 'banana', 'cherry'}
    set2 = {'banana', 'cherry', 'date'}

    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    symmetric_difference_set = set1.symmetric_difference(set2)

    return union_set, intersection_set, symmetric_difference_set

if __name__ == '__main__':
    union_result, intersection_result, symmetric_difference_result = set_operations()
    print("Union:", union_result)
    print("Intersection:", intersection_result)
    print("Symmetric Difference:", symmetric_difference_result)