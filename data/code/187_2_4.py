def get_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    maximum = data[0]
    for element in data[1:]:
        if element > maximum:
            maximum = element
    return maximum
if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, 0.577, -1.0]
    result = get_maximum(sample_list)
    print(result)