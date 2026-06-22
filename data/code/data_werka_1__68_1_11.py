def find_element_differences(list1, list2):
    return [abs(a - b) for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [5, 3, 9, 1]
    sample_list2 = [2, 7, 4, 6]
    result = find_element_differences(sample_list1, sample_list2)
    print(result)