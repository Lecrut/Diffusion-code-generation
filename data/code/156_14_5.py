def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    result1 = calculate_average(data1)
    print(f"Average of {data1}: {result1}")
    data2 = [10, 20, 30, 40, 50, 60]
    result2 = calculate_average(data2)
    print(f"Average of {data2}: {result2}")
    data3 = [1.5, 2.5, 3.5]
    result3 = calculate_average(data3)
    print(f"Average of {data3}: {result3}")
    data4 = []
    result4 = calculate_average(data4)
    print(f"Average of {data4}: {result4}")