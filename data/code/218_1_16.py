MIN_VALUE = float('inf')

def find_minimum(data):
    if not data:
        raise ValueError("Input tuple cannot be empty")
    minimum = MIN_VALUE
    for element in data:
        if element < minimum:
            minimum = element
    return minimum

if __name__ == '__main__':
    sample_tuple = (3, 1, 4, 1, 5, 9, 2, 6)
    result = find_minimum(sample_tuple)
    print(result)