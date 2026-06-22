def get_first_value(data_tuple):
    return data_tuple[0]

if __name__ == '__main__':
    sample_values = (10, 20, 30, 40, 50)
    first_value = get_first_value(sample_values)
    print(first_value)