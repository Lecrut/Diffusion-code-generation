def find_common_elements(list1, list2):
    common = [element for element in list1 if element in list2]
    return common

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = [40, 50, 60, 70, 80]
    result = find_common_elements(sample_list1, sample_list2)
    print(result)