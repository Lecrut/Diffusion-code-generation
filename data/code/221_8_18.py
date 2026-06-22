def order_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers) or len(numbers) != 3:
        raise ValueError("Input must be a list of exactly three numbers.")
    sorted_numbers = sorted(numbers)
    return sorted_numbers

if __name__ == '__main__':
    sample_numbers = [56, 12, 45]
    print(order_numbers(sample_numbers))