import statistics
def find_median(data: list[float]) -> float:
    if not data:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2.0
if __name__ == '__main__':
    sample1 = [3.14, 1.618, 2.718, 0.577]
    sample2 = [5.0, 2.0, 9.0, 1.0, 4.0]
    sample3 = [10.5, 2.5, 5.5, 7.5]
    sample4 = [1.1, 2.2, 3.3, 4.4, 5.5]
    print(f"Median of {sample1}: {find_median(sample1)}")
    print(f"Median of {sample2}: {find_median(sample2)}")
    print(f"Median of {sample3}: {find_median(sample3)}")
    print(f"Median of {sample4}: {find_median(sample4)}")