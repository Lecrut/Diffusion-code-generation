def validate_input(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")

def find_maximum(data):
    validate_input(data)
    max_value = data[0]
    for value in data[1:]:
        if value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, 0.577, 9.999, -1.0, 5.0]
    try:
        maximum = find_maximum(sample_list)
        print(maximum)
    except ValueError as e:
        print(e)