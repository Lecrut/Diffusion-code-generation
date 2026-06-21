def compute_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

if __name__ == '__main__':
    data1 = (10, 20, 30, 40, 50)
    print(f"Average of {data1}: {compute_average(data1)}")
    data2 = [5, 15, 25, 35]
    print(f"Average of {data2}: {compute_average(data2)}")
    data3 = []
    print(f"Average of {data3}: {compute_average(data3)}")
    data4 = [7]
    print(f"Average of {data4}: {compute_average(data4)}")