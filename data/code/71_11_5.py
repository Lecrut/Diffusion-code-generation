def find_middle(data):
    n = len(data)
    middle_index = n // 2
    return data[middle_index]
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    middle_element = find_middle(sample_list)
    print(middle_element)
    sample_list_even = [10, 20, 30, 40]
    middle_element_even = find_middle(sample_list_even)
    print(middle_element_even)
    sample_list_large = list(range(1000))
    middle_element_large = find_middle(sample_list_large)
    print(middle_element_large)