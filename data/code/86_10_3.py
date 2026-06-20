def compare_booleans(a: bool, b: bool) -> str:
    result = 'Equal' if a == b else 'Different'
    return result

if __name__ == '__main__':
    sample1 = True
    sample2 = False
    sample3 = False
    sample4 = True
    
    print(compare_booleans(sample1, sample2))
    print(compare_booleans(sample2, sample3))
    print(compare_booleans(sample3, sample4))
    print(compare_booleans(sample4, sample1))