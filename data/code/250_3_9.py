def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    numbers = [10, 20, 30, 40]
    print(calculate_average(numbers))