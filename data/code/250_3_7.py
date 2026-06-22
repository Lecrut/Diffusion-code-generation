def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    numbers = [15, 25, 35, 45, 55]
    average = calculate_average(numbers)
    print(average)