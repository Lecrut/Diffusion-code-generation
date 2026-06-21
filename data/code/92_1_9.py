def find_opposite_truth(truth: bool) -> bool:
    if truth is True:
        return False
    if truth is False:
        return True
    raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    val1 = True
    out1 = find_opposite_truth(val1)
    print(out1)
    val2 = False
    out2 = find_opposite_truth(val2)
    print(out2)