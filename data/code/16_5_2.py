def get_initial_value(values):
    return values[0]

if __name__ == '__main__':
    sample_list = [42, 10, 7, 3, 99]
    result = get_initial_value(sample_list)
    print(result)