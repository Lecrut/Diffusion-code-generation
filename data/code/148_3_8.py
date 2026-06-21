def find_largest(data):
    if not isinstance(data, list) or not data:
        raise ValueError("Input must be a non-empty list")
    return max(data)

if __name__ == '__main__':
    sample1 = [10, 5, 20, 8]
    print(f"Largest in {sample1}: {find_largest(sample1)}")

    sample2 = [-5, -1, -10, -2]
    print(f"Largest in {sample2}: {find_largest(sample2)}")

    sample3 = [3.14, 2.71, 1.618]
    print(f"Largest in {sample3}: {find_largest(sample3)}")

    sample4 = [42]
    print(f"Largest in {sample4}: {find_largest(sample4)}")