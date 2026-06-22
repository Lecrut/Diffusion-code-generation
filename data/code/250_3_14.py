def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    numbers = [3, 6, 9, 12]
    avg = calculate_average(numbers)
    print(avg)