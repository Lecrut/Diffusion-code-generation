MAX_VALUE = float('inf')

def find_largest_value(dictionary):
    return max(dictionary.values(), default=MAX_VALUE)

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 5, 'c': 2}
    print(find_largest_value(sample_dict))