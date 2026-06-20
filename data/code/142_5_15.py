def are_booleans_equal(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    sample1 = True
    sample2 = False
    result = are_booleans_equal(sample1, sample2)
    print(f"Sample 1: {sample1}, Sample 2: {sample2}, Result: {result}")