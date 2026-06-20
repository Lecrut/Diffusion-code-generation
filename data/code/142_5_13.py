def compare_boolean_values(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    sample1 = True
    sample2 = False
    result = compare_boolean_values(sample1, sample2)
    print(f"Sample 1: {sample1}, Sample 2: {sample2}, Result: {result}")