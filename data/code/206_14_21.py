MIN_VALUE_LAMBDA = lambda lst: min(lst) if lst else None

if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5]
    sample2 = [7]
    sample3 = []
    print(f"Minimum in {sample1}: {MIN_VALUE_LAMBDA(sample1)}")
    print(f"Minimum in {sample2}: {MIN_VALUE_LAMBDA(sample2)}")
    print(f"Minimum in {sample3}: {MIN_VALUE_LAMBDA(sample3)}")