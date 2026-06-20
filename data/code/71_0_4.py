def find_middle_element(data):
    n = len(data)
    middle_index = n // 2
    return data[middle_index]
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [10, 20, 30, 40]
    print(find_middle_element(sample_list1))
    print(find_middle_element(sample_list2))