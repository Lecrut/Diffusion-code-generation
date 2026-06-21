def shared_elements(list1, list2):
    set1 = set(list1)
    return [item for item in list2 if item in set1]

if __name__ == '__main__':
    print(shared_elements([1, 2, 3, 4], [3, 4, 5, 6]))