def find_opposite_truth(value):
    if value is True:
        return False
    if value is False:
        return True
    raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    result1 = find_opposite_truth(True)
    result2 = find_opposite_truth(False)
    print(result1)
    print(result2)