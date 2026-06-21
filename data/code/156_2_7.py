def validate_data(data):
    if not all(isinstance(x, int) for x in data):
        raise ValueError("All elements must be integers")
    if not data:
        return 0

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    average = calculate_average(validate_data(sample_numbers))
    print(average)