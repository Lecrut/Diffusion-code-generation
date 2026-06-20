def check_both_true(a: bool, b: bool) -> bool:
    return a & b

if __name__ == '__main__':
    sample_a = False
    sample_b = True
    result = check_both_true(sample_a, sample_b)
    print(f"check_both_true({sample_a}, {sample_b}): {result}")