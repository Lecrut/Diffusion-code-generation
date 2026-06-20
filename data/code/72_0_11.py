def compare_elements(list1, list2, index):
    try:
        return list1[index], list2[index]
    except IndexError:
        return None, None

if __name__ == '__main__':
    print(compare_elements([1, 2, 3], ['a', 'b', 'c'], 1))
    print(compare_elements([1, 2], ['a', 'b', 'c'], 2))