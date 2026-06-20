def compare_elements(list1, list2, index):
    return list1[index] <= list2[index]
if __name__ == '__main__':
    result = compare_elements([1, 2, 3], [4, 5, 6], 1)
    print(result)