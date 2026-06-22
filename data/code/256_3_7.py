def find_range(data):
    if not data:
        raise ValueError("Input set cannot be empty")
    return max(data) - min(data)

if __name__ == '__main__':
    sample_set1 = {1, 5, 2, 8, 3}
    sample_set2 = {10, 4, 7, 1, 9}
    sample_set3 = set()
    sample_set4 = {5}

    print(f"Range of {sample_set1}: {find_range(sample_set1)}")
    print(f"Range of {sample_set2}: {find_range(sample_set2)}")
    try:
        print(f"Range of {sample_set3}: {find_range(sample_set3)}")
    except ValueError as e:
        print(f"Error for {sample_set3}: {e}")
    print(f"Range of {sample_set4}: {find_range(sample_set4)}")