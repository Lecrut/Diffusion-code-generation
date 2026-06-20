def find_middle_element(data):
    n = len(data)
    middle_index = (n - 1) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_list1 = [3, 5, 7, 9, 11]
    sample_list2 = [40, 60, 80]
    sample_list3 = [-5, -2, 0, 2, 5]
    print(f"Middle element of {sample_list1}: {find_middle_element(sample_list1)}")
    print(f"Middle element of {sample_list2}: {find_middle_element(sample_list2)}")
    print(f"Middle element of {sample_list3}: {find_middle_element(sample_list3)}")