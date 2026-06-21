sample_dict = {'a': 3, 'b': 5, 'c': 2}

def find_highest_value(dictionary):
    return max(dictionary.values())

if __name__ == '__main__':
    print(find_highest_value(sample_dict))