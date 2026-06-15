def calculate_sum(numbers):
    total = 0
    for num in numbers:
        if isinstance(num, int) or isinstance(num, float):
            total += num
        else:
            print(f"Error: '{num}' is not a valid number.")
    return total
if __name__ == '__main__':
    sample_numbers = [10, 5.5, 20, "a", 3.5]
    print("Input list:", sample_numbers)
    result = calculate_sum(sample_numbers)
    print("Total sum:", result)