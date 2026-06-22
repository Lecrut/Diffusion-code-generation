def calculate_mean(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

if __name__ == '__main__':
    data1 = [10, 20, 30, 40, 50]
    data2 = [5.5, 6.5, 7.5]
    data3 = []
    print(f"Mean of {data1}: {calculate_mean(data1)}")
    print(f"Mean of {data2}: {calculate_mean(data2)}")
    print(f"Mean of {data3}: {calculate_mean(data3)}")