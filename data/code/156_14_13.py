import math

def calculate_average(numbers):
    if not numbers:
        return 0
    total = math.fsum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    sample2 = [10, 20, 30, 40, 50, 60]
    sample3 = []
    sample4 = [1.5, 2.5, 3.5]

    avg1 = calculate_average(sample1)
    avg2 = calculate_average(sample2)
    avg3 = calculate_average(sample3)
    avg4 = calculate_average(sample4)

    print(f"Average of {sample1}: {avg1}")
    print(f"Average of {sample2}: {avg2}")
    print(f"Average of {sample3}: {avg3}")
    print(f"Average of {sample4}: {avg4}")