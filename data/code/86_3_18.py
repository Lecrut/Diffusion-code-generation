def compare_booleans(a, b):
    return [a == b]

if __name__ == '__main__':
    sample1 = (True, False)
    print(compare_booleans(*sample1))
    
    sample2 = (True, True)
    print(compare_booleans(*sample2))
    
    sample3 = (False, True)
    print(compare_booleans(*sample3))