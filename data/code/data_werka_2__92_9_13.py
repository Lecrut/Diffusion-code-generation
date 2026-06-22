def find_opposite_truth(value):
    if value is True:
        return False
    if value is False:
        return True
    raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    print(find_opposite_truth(True))
    print(find_opposite_truth(False))