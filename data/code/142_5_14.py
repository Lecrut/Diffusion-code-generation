def check_same_truth_value(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = check_same_truth_value(sample_a, sample_b)
    print(result)