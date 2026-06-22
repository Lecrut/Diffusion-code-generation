def find_largest_in_dict(d):
    return max(d.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 5}
    result = find_largest_in_dict(sample_dict)
    print(result)