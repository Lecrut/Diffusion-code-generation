def calculate_mean(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

if __name__ == '__main__':
    data1 = [15, 25, 35, 45, 55]
    result1 = calculate_mean(data1)
    print(f"Mean of {data1}: {result1}")