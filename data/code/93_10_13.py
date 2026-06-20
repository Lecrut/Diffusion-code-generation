def check_both_false(a: bool, b: bool) -> bool:
    return not (a or b)

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = check_both_false(sample_a, sample_b)
    print(result)