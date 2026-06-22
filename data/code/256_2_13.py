def calculate_range(data):
    if not data:
        return None
    minimum = min(data)
    maximum = max(data)
    return maximum - minimum

if __name__ == '__main__':
    sample1 = [1, 5, 2, 8, 3]
    sample2 = [100, 50, 200, 10]
    sample3 = []
    sample4 = [7]

    print(f"Range of {sample1}: {calculate_range(sample1)}")
    print(f"Range of {sample2}: {calculate_range(sample2)}")
    print(f"Range of {sample3}: {calculate_range(sample3)}")
    print(f"Range of {sample4}: {calculate_range(sample4)}")