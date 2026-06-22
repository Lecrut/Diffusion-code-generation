def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    result = calculate_mean(data)
    print(result)