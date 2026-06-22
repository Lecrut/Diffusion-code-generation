def negate(value):
    if value is True:
        return False
    if value is False:
        return True
    raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    result_true = negate(True)
    result_false = negate(False)
    print(result_true)
    print(result_false)