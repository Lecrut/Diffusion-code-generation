def find_largest_value(d):
    return max(d.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 5, 'c': 20}
    result = find_largest_value(sample_dict)
    print(result)