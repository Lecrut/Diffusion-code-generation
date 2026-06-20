def compare_booleans(a: bool, b: bool) -> str:
    return "True" if a == b else "False"

if __name__ == '__main__':
    sample1 = True
    sample2 = False
    result = compare_booleans(sample1, sample2)
    print(result)