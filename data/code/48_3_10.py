def find_largest_element(data):
    return max(data.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 25, 'c': 5, 'd': 100}
    print(find_largest_element(sample_dict))