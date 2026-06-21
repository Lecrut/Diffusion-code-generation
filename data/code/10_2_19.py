def is_valid_tuple(data):
    return isinstance(data, tuple) and len(data) == 5 and all(isinstance(x, (int, float)) for x in data)

def initialize_and_output():
    values = (1, 2, 3, 4, 5)
    if not is_valid_tuple(values):
        raise ValueError("Invalid tuple")
    return values[0]

if __name__ == '__main__':
    print(initialize_and_output())