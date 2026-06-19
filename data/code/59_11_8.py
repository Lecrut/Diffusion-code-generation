def find_middle_element(sequence):
    n = len(sequence)
    if n == 0:
        return None
    middle_index = n // 2
    return sequence[middle_index]

if __name__ == '__main__':
    list1 = [7, 8, 9]
    list2 = [10, 20, 30, 40]
    list3 = [42]
    list4 = []
    print(find_middle_element(list1))
    print(find_middle_element(list2))
    print(find_middle_element(list3))
    print(find_middle_element(list4))