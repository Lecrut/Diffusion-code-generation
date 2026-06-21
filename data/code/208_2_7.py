def calculate_mean(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
        raise ValueError("Input must be a list of integers")
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(calculate_mean(sample_values))
    empty_list = []
    print(calculate_mean(empty_list))