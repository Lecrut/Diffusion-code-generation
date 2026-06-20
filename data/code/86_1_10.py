def compare_booleans(a, b):
    result = 'True' if a == b else 'False'
    return result

if __name__ == '__main__':
    sample1 = compare_booleans(True, True)
    sample2 = compare_booleans(False, False)
    sample3 = compare_booleans(True, False)
    print(sample1)
    print(sample2)
    print(sample3)