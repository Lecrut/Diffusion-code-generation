def compare_elements(list1, list2, index):
    return list1[index] <= list2[index]
if __name__ == '__main__':
    result = compare_elements([3, 5, 7], [4, 2, 9], 1)
    print(result)