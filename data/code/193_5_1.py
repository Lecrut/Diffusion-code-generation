def calculate_sum(numbers):
    total = 0
    for num in numbers:
        if isinstance(num, int) or isinstance(num, float):
            total += num
        else:
            print(f"Error: Invalid input '{num}'. Only numbers are allowed.")
            return None
    return total
if __name__ == '__main__':
    sample_numbers = [10, 5.5, 20, "a", 3.5]
    result = calculate_sum(sample_numbers)
    if result is not None:
        print(f"The sum of the valid numbers is: {result}")