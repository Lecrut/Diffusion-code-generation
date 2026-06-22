def find_largest_value(dictionary):
    return max(dictionary.values(), default=None)

if __name__ == '__main__':
    sample_dict = {'x': 10, 'y': 20, 'z': 5}
    print(find_largest_value(sample_dict))