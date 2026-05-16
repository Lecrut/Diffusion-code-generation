def compute_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    result1 = compute_average(sample1)
    print(f"Average of {sample1}: {result1}")
    sample2 = (10, 20, 30, 40)
    result2 = compute_average(sample2)
    print(f"Average of {sample2}: {result2}")
    sample3 = [5.5, 1.5, 3.0]
    result3 = compute_average(sample3)
    print(f"Average of {sample3}: {result3}")
    sample4 = []
    result4 = compute_average(sample4)
    print(f"Average of {sample4}: {result4}")