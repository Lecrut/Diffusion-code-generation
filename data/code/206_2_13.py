def find_min_value(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = float('inf')
    for number in data:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, -0.5, 9.99]
    result = find_min_value(sample_list)
    print(result)