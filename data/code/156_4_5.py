def compute_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    result1 = compute_average(sample1)
    print(f"The average of {sample1} is: {result1}")
    sample2 = (10, 20, 30)
    result2 = compute_average(sample2)
    print(f"The average of {sample2} is: {result2}")
    sample3 = []
    result3 = compute_average(sample3)
    print(f"The average of {sample3} is: {result3}")
    sample4 = [5.5, 6.5, 7.5]
    result4 = compute_average(sample4)
    print(f"The average of {sample4} is: {result4}")