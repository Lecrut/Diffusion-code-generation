def calculate_mean(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    data1 = [10, 20, 30, 40, 50]
    data2 = [5, 15, 25, 35, 45, 55]
    data3 = []
    mean1 = calculate_mean(data1)
    mean2 = calculate_mean(data2)
    mean3 = calculate_mean(data3)
    print(f"Mean of {data1}: {mean1}")
    print(f"Mean of {data2}: {mean2}")
    print(f"Mean of {data3}: {mean3}")