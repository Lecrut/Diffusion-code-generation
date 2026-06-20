def negate_boolean(value):
    return not value

if __name__ == '__main__':
    sample1 = True
    result1 = negate_boolean(sample1)
    print(f"Input: {sample1}, Output: {result1}")
    sample2 = False
    result2 = negate_boolean(sample2)
    print(f"Input: {sample2}, Output: {result2}")