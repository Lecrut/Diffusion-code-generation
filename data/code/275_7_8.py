def filter_even_second_elements(tuples_list):
    return [t for t in tuples_list if t[1] % 2 == 0]

if __name__ == '__main__':
    sample_data = [(1, 3), (4, 6), (7, 9), (10, 12)]
    filtered_data = filter_even_second_elements(sample_data)
    print(filtered_data)