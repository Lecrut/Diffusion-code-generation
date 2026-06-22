def get_last_element(data_list):
    if not data_list:
        return None
    return next(reversed(data_list))

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_element(sample_list)
    print(result)