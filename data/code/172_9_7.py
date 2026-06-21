lookup = ['one', 'two', 'three', 'four', 'five']

def initialize_dict():
    result = {}
    for i in range(5):
        result[i] = lookup[i]
    return result

if __name__ == '__main__':
    print(initialize_dict())