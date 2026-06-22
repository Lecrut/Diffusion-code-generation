def calculate_range(numbers):
    try:
        numbers = [int(num) for num in numbers.split()]
        return max(numbers) - min(numbers)
    except ValueError:
        return "Invalid input"

if __name__ == '__main__':
    sample_input = "10 20 30 40"
    print(calculate_range(sample_input))