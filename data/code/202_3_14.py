def find_highest_value(data):
    return max(data.values())

if __name__ == '__main__':
    sample_data = {'a': 3, 'b': 5, 'c': 2}
    print(find_highest_value(sample_data))