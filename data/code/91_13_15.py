def negate_boolean(b):
    return int(not b)
if __name__ == '__main__':
    sample1 = True
    result1 = negate_boolean(sample1)
    print(result1)
    sample2 = False
    result2 = negate_boolean(sample2)
    print(result2)