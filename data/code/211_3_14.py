def set_operations():
    set1 = {'apple', 'banana', 'cherry'}
    set2 = {'banana', 'cherry', 'date'}

    intersection_result = set1.intersection(set2)
    union_result = set1.union(set2)
    symmetric_difference_result = set1.symmetric_difference(set2)

    return intersection_result, union_result, symmetric_difference_result

if __name__ == '__main__':
    intersection, union, symmetric_diff = set_operations()
    print(f"Intersection: {intersection}")
    print(f"Union: {union}")
    print(f"Symmetric Difference: {symmetric_diff}")