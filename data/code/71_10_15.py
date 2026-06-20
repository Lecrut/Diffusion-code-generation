MIDDLE_INDEX_CALCULATION = lambda n: (n - 1) // 2

def find_middle_element(data):
    return data[MIDDLE_INDEX_CALCULATION(len(data))]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [10, 20, 30, 40]
    sample_list3 = [100]
    sample_list4 = [5, 15, 25, 35, 45, 55]
    print(find_middle_element(sample_list1))
    print(find_middle_element(sample_list2))
    print(find_middle_element(sample_list3))
    print(find_middle_element(sample_list4))