def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    maximum = data[0]
    for number in data:
        if number > maximum:
            maximum = number
    return maximum
if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, 0.577, 9.81]
    max_value = find_maximum(sample_list)
    print(max_value)