def compare_booleans(a: bool, b: bool) -> str:
    if a == b:
        return 'Equal'
    else:
        return 'Different'

if __name__ == '__main__':
    sample1 = True
    sample2 = False
    sample3 = True
    sample4 = False
    print(compare_booleans(sample1, sample2))
    print(compare_booleans(sample2, sample3))
    print(compare_booleans(sample3, sample4))
    print(compare_booleans(sample4, sample1))