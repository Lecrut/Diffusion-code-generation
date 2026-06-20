def compare_lists(list1, list2):
    return [x == y for x, y in zip(list1, list2)]

if __name__ == '__main__':
    result = compare_lists([1, 2, 3], [1, 2, 4])
    print(result)