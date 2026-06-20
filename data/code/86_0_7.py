def compare_booleans(a: bool, b: bool) -> str:
    return "True" if a == b else "False"

if __name__ == '__main__':
    sample_a = True
    sample_b = True
    result = compare_booleans(sample_a, sample_b)
    print(result)