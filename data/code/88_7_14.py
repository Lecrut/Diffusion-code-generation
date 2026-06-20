def both_true(a: bool, b: bool) -> str:
    if a and b:
        return "Both are true"
    else:
        return "At least one is false"

if __name__ == '__main__':
    sample1 = both_true(True, True)
    sample2 = both_true(False, False)
    
    print(sample1)
    print(sample2)