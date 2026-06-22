def get_middle_value(values):
    mid_index = len(values) // 2
    return values[mid_index]

if __name__ == '__main__':
    sample_data_1 = [10, 20, 30, 40, 50]
    sample_data_2 = [5, 15, 25, 35, 45, 55]
    sample_data_3 = [1, 2, 3]
    sample_data_4 = [99]
    
    print(get_middle_value(sample_data_1))
    print(get_middle_value(sample_data_2))
    print(get_middle_value(sample_data_3))
    print(get_middle_value(sample_data_4))