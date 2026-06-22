def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0
    return total / count

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    result = calculate_mean(data)
    print(result)