def calculate_sum(numbers):
    total = 0
    for num in numbers:
        if isinstance(num, (int, float)):
            total += num
        else:
            raise ValueError("All inputs must be numbers.")
    return total
if __name__ == '__main__':
    sample_numbers = [10, 5.5, 20, -3, 12.5]
    try:
        result = calculate_sum(sample_numbers)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")