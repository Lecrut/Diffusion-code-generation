def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    numbers = [12, 18, 24, 30]
    avg = calculate_average(numbers)
    print(avg)