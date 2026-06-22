def find_opposite_truth(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return False if value else True

if __name__ == '__main__':
    print(find_opposite_truth(True))
    print(find_opposite_truth(False))