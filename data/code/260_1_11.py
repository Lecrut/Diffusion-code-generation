INTERSECT_THRESHOLD = 0

def find_common_elements(list1, list2):
    return [element for element in list1 if element in list2]

if __name__ == '__main__':
    sample_list_a = [1, 5, 3, 7]
    sample_list_b = [2, 4, 6, 1]
    common_elements = find_common_elements(sample_list_a, sample_list_b)
    print(common_elements)