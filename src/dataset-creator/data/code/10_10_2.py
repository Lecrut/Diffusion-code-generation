def calculate_sum(numbers):
    total = 0
    for num in numbers:
        if isinstance(num, (int, float)):
            total += num
        else:
            raise ValueError("Invalid input: only numbers are allowed.")
    return total
if __name__ == '__main__':
    sample_numbers = [10, 25.5, 30, 4.5, "error", 50]
    validated_numbers = []
    for item in sample_numbers:
        if isinstance(item, (int, float)):
            validated_numbers.append(item)
        else:
            print(f"Skipping invalid input: {item}")
    try:
        result = calculate_sum(validated_numbers)
        print(f"The sum of the valid numbers is: {result}")
    except ValueError as e:
        print(f"Error during calculation: {e}")