import statistics

def get_median(sequence):
    return statistics.median(sequence)

if __name__ == '__main__':
    sample_data_1 = [7, 1, 3, 5, 9]
    sample_data_2 = [4, 8, 2, 6]
    sample_data_3 = [10]
    sample_data_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    result_1 = get_median(sample_data_1)
    result_2 = get_median(sample_data_2)
    result_3 = get_median(sample_data_3)
    result_4 = get_median(sample_data_4)

    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)