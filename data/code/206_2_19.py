def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    min_value = data[0]
    for number in data:
        if number < min_value:
            min_value = number
    return min_value

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, -0.5, 9.99]
    result = find_minimum(sample_list)
    print(result)