def filter_positive_numbers(data):
    return [x for x in data if x >= 0]
if __name__ == '__main__':
    sample_data = [-5, -1, 3, 7, -2, 9, 0, -8, 4]
    result = filter_positive_numbers(sample_data)
    print(result)