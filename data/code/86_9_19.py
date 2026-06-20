def compare_booleans(a: bool, b: bool) -> str:
    return f"The values are equal: {a == b}"

if __name__ == '__main__':
    sample_a = False
    sample_b = False
    result = compare_booleans(sample_a, sample_b)
    print(result)