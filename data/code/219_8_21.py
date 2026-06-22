def validate_input(value):
    if not isinstance(value, int) or value < 1:
        raise ValueError("Input must be a positive integer")

def find_max_squared():
    validate_input(100)
    return max(x**2 for x in range(1, 101))

if __name__ == '__main__':
    max_value = find_max_squared()
    print(max_value)