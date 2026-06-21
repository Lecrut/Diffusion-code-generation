def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

if __name__ == '__main__':
    data1 = [3, 6, 9, 12]
    data2 = [7, 14, 21, 28, 35]
    data3 = []
    print(f"Average of {data1}: {calculate_average(data1)}")
    print(f"Average of {data2}: {calculate_average(data2)}")
    print(f"Average of {data3}: {calculate_average(data3)}")