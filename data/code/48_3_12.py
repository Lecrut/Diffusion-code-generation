def find_max_value(data):
    return max(data.values())

if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 42, 'c': 7, 'd': 15}
    print(find_max_value(sample_data))