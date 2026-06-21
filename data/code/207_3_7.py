def find_highest_value(data):
    return max(data.values())

if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 20, 'c': 5, 'd': 30}
    result = find_highest_value(sample_data)
    print(result)