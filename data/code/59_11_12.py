def find_middle_element(sequence):
    n = len(sequence)
    if n == 0:
        return None
    middle_index = n // 2
    return sequence[middle_index]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50, 60]
    list3 = [1, 2, 3, 4]
    list4 = [100]
    list5 = []
    print(find_middle_element(list1))
    print(find_middle_element(list2))
    print(find_middle_element(list3))
    print(find_middle_element(list4))
    print(find_middle_element(list5))