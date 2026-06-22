def find_element_differences(list1, list2):
    return [abs(a - b) for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40]
    sample_list2 = [15, 18, 35, 40]
    result = find_element_differences(sample_list1, sample_list2)
    print(result)