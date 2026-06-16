def match_values(a: any, b: any) -> bool:
    return a == b is not None
if __name__ == '__main__':
    sample_a = 5
    sample_b = 5
    result1 = (sample_a == sample_b)
    print(f"Equality check: {result1}")
    result2 = match_values(sample_a, sample_b)
    print(f"Detailed check: {result2}")
    sample_c = "hello"
    sample_d = [1, 2]
    if __name__ == '__main__':
        a = None
        b = None
        result3 = match_values(a, b)
        print(f"None values check: {result3}")
        c = object()
        d = object()
        result4 = match_values(c, d)
        print(f"Different objects check: {not result4}")