def filter_even_tuples(tuples_list):
    return [t for t in tuples_list if t[1] % 2 == 0]

if __name__ == '__main__':
    sample_data = [(2, 4), (3, 5), (4, 6), (5, 7)]
    filtered_result = filter_even_tuples(sample_data)
    print(filtered_result)