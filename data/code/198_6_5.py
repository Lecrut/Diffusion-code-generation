def find_smallest_first_element(tuples_list):
    return min(tuples_list, key=lambda x: x[0])

if __name__ == '__main__':
    sample_data = [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
    print(find_smallest_first_element(sample_data))