def find_max_element(sorted_list):
    return sorted_list[-1]

if __name__ == '__main__':
    sample_list = [7, 3, 9, 5, 2]
    max_element = find_max_element(sample_list)
    print(max_element)