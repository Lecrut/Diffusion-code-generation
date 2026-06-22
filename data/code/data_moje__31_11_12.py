SIDE_LENGTH_CONSTANT = 15

def compute_area(side):
    if side < 0:
        raise ValueError("Side length must be non-negative")
    return side * side

if __name__ == '__main__':
    side_value = SIDE_LENGTH_CONSTANT
    result = compute_area(side_value)
    print(result)