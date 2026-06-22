def filter_even_second_elements(tuples_list):
    filtered_tuples = [t for t in tuples_list if t[1] % 2 == 0]
    return filtered_tuples

if __name__ == '__main__':
    sample_data = [(4, 8), (9, 3), (5, 6), (7, 4)]
    result = filter_even_second_elements(sample_data)
    print(result)