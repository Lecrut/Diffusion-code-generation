def find_largest_value(d):
    return max(d.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 25, 'c': 15, 'd': 50, 'e': 30}
    print(find_largest_value(sample_dict))