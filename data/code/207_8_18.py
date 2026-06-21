def find_max_element(sorted_list):
    if not sorted_list:
        raise ValueError("The list is empty")
    return sorted_list[-1]

if __name__ == '__main__':
    sample_list = [3, 5, 2, 8, 1]
    print(find_max_element(sample_list))