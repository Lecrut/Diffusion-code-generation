def check_same_truth_value(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    sample1 = True
    sample2 = False
    result = check_same_truth_value(sample1, sample2)
    print(f"Sample 1: {sample1}, Sample 2: {sample2}, Same Truth Value: {result}")