def find_smallest_element(data):
    sorted_data = sorted(data)
    smallest_element = sorted_data[0]
    return smallest_element

if __name__ == '__main__':
    sample_list = [3.14, -1.5, 2.718, -9.8, 0.001, 5.0]
    result = find_smallest_element(sample_list)
    print(result)