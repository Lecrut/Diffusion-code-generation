def calculate_range(numbers):
    try:
        numbers = list(map(int, numbers.split()))
        return max(numbers) - min(numbers)
    except ValueError:
        return None

if __name__ == '__main__':
    sample_input = "10 20 30 40"
    print(calculate_range(sample_input))