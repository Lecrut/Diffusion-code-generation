def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    numbers = [15, 25, 35, 45]
    avg = calculate_average(numbers)
    print(avg)