def get_first_value(data_list):
    iterator = iter(data_list)
    return next(iterator)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40]
    print(get_first_value(sample_values))