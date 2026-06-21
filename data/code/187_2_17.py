def validate_input(data):
    if not data:
        raise ValueError("Input list cannot be empty")

def find_maximum(data):
    validate_input(data)
    maximum = data[0]
    for element in data[1:]:
        if element > maximum:
            maximum = element
    return maximum

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, 0.577, 9.99]
    result = find_maximum(sample_list)
    print(result)