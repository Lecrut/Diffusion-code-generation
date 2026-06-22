def get_penultimate_value(data_list):
    if len(data_list) < 2:
        raise ValueError("List must contain at least two elements")
    return data_list[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_penultimate_value(sample_list))
    short_list = [1, 2]
    print(get_penultimate_value(short_list))
    try:
        print(get_penultimate_value([1]))
    except ValueError as e:
        print(e)