lookup = ['one', 'two', 'three', 'four', 'five']

def initialize_dict():
    result = {}
    for i in range(1, len(lookup) + 1):
        result[i] = lookup[i - 1]
    return result

if __name__ == '__main__':
    sample_dict = initialize_dict()
    print(sample_dict)