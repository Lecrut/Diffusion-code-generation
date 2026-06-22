def find_range(data):
    if not data:
        return None
    minimum = min(data)
    maximum = max(data)
    return maximum - minimum

if __name__ == '__main__':
    sample1 = [3.5, 2.1, 4.8, 1.9]
    sample2 = [100.2, 50.7, 200.3, 10.4]
    sample3 = []
    sample4 = [5.5]

    print(f"Range of {sample1}: {find_range(sample1)}")
    print(f"Range of {sample2}: {find_range(sample2)}")
    print(f"Range of {sample3}: {find_range(sample3)}")
    print(f"Range of {sample4}: {find_range(sample4)}")