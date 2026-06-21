def find_max_element(sorted_list):
    return sorted_list[-1]

if __name__ == '__main__':
    sample_data = [7, 3, 9, 15, 2]
    max_value = find_max_element(sample_data)
    print(max_value)