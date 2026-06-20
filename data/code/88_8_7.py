def check_both_true(a: bool, b: bool) -> bool:
    result = a and b
    return result

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    print(check_both_true(sample_a, sample_b))