def get_first_value(values):
    iterator = iter(values)
    return next(iterator)

if __name__ == '__main__':
    data_list = [42, 100, 7, 25]
    print(get_first_value(data_list))