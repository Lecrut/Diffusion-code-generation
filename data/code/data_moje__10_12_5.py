def get_first_value(data: list) -> object:
    iterator = iter(data)
    return next(iterator)

if __name__ == '__main__':
    sample_list = [42, 15, 99]
    result = get_first_value(sample_list)
    print(result)