def find_largest_value(dictionary):
    return max(dictionary.values(), default=None)

if __name__ == '__main__':
    sample_dict = {'m': 15, 'n': 25, 'o': 30}
    print(find_largest_value(sample_dict))