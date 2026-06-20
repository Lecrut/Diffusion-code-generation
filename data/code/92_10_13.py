def validate_input(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")

def find_opposite_truth(value):
    validate_input(value)
    return not value

if __name__ == '__main__':
    print(find_opposite_truth(True))
    print(find_opposite_truth(False))