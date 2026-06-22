def negate(flag):
    if flag is True:
        return False
    if flag is False:
        return True
    raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    result_a = negate(False)
    result_b = negate(True)
    print(result_a)
    print(result_b)