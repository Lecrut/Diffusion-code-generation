MIN_VALUE = float('inf')

def find_minimum(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    minimum = MIN_VALUE
    for item in data:
        if item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8]
    result = find_minimum(sample_list)
    print(result)