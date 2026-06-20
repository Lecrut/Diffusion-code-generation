def is_valid_boolean(value):
    return isinstance(value, bool)

def opposite_truth(value):
    if not is_valid_boolean(value):
        raise ValueError("Input must be a boolean")
    return not value

if __name__ == '__main__':
    print(opposite_truth(True))
    print(opposite_truth(False))