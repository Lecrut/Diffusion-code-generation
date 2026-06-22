def find_common_elements(list1, list2):
    return [element for element in list1 if element in list2]

def print_common_elements(list1, list2):
    common = find_common_elements(list1, list2)
    for element in common:
        print(element)
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    print_common_elements(sample_list1, sample_list2)