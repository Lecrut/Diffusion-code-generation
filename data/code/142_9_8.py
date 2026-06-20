def compare_booleans(x: bool, y: bool) -> bool:
    comparison_result = x == y
    return comparison_result
if __name__ == '__main__':
    sample1_a = True
    sample1_b = False
    print(compare_booleans(sample1_a, sample1_b))
    sample2_a = False
    sample2_b = True
    print(compare_booleans(sample2_a, sample2_b))
    sample3_a = True
    sample3_b = True
    print(compare_booleans(sample3_a, sample3_b))