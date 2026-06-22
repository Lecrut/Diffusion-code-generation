def find_unique_elements(list1, list2):
    return [element for element in list1 if element not in list2] + [element for element in list2 if element not in list1]

if __name__ == '__main__':
    sample_list1 = [1.1, 2.2, 3.3, 4.4]
    sample_list2 = [3.3, 4.4, 5.5, 6.6]
    print(find_unique_elements(sample_list1, sample_list2))