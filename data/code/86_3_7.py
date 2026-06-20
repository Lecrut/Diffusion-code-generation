def compare_booleans(a, b):
    return [a == b]

if __name__ == '__main__':
    sample1 = [True, True]
    result1 = compare_booleans(sample1[0], sample1[1])
    print(result1)
    
    sample2 = [False, False]
    result2 = compare_booleans(sample2[0], sample2[1])
    print(result2)
    
    sample3 = [True, False]
    result3 = compare_booleans(sample3[0], sample3[1])
    print(result3)