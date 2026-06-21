def get_last_element(data_list):
    reversed_iterator = reversed(data_list)
    return next(reversed_iterator)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_element(sample_list)
    print(result)