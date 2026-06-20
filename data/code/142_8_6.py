def validate_booleans(bool1, bool2):
    if not isinstance(bool1, bool) or not isinstance(bool2, bool):
        raise ValueError("Both arguments must be boolean values.")
    return True

def compare_booleans(bool1, bool2):
    validate_booleans(bool1, bool2)
    return bool1 == bool2

if __name__ == '__main__':
    sample1 = True
    sample2 = False
    result = compare_booleans(sample1, sample2)
    print(result)