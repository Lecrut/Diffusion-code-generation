def are_booleans_identical(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    sample1_a = True
    sample1_b = True
    result1 = are_booleans_identical(sample1_a, sample1_b)
    print(result1)

    sample2_a = False
    sample2_b = False
    result2 = are_booleans_identical(sample2_a, sample2_b)
    print(result2)

    sample3_a = True
    sample3_b = False
    result3 = are_booleans_identical(sample3_a, sample3_b)
    print(result3)