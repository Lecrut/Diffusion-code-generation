def get_max_value(data):
    return max(data.values())

if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 25, 'c': 15, 'd': 30}
    result = get_max_value(sample_data)
    print(result)