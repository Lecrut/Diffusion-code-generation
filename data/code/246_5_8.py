def validate_input(a, b):
    try:
        return float(a), float(b)
    except ValueError:
        raise TypeError("Both inputs must be numeric.")

def add(a, b):
    num_a, num_b = validate_input(a, b)
    return num_a + num_b

if __name__ == '__main__':
    print(add(10, 5))
    print(add("12.5", 3.5))