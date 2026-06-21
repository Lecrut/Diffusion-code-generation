import statistics

def calculate_median(numbers):
    return statistics.median(numbers)

if __name__ == '__main__':
    data1 = [3, 1, 2]
    data2 = [4, 2, 5, 3]
    data3 = [9, 7, 8, 6, 5]

    print(f"Median of {data1}: {calculate_median(data1)}")
    print(f"Median of {data2}: {calculate_median(data2)}")
    print(f"Median of {data3}: {calculate_median(data3)}")