def get_middle_value(values):
    index = len(values) // 2
    return values[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle_value(sample_list)
    print(result)