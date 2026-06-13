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
    sample_input = [10, 5.5, 20, "a", 3.5]
    numbers_to_sum = []
    error_occurred = False
    for item in sample_input:
        try:
            if isinstance(item, str):
                raise ValueError("String encountered")
            numbers_to_sum.append(float(item))
        except ValueError:
            print(f"Error: Could not convert '{item}' to a number. Skipping this item.")
            error_occurred = True
    if not error_occurred:
        result = calculate_sum(numbers_to_sum)
        if result is not None:
            print(result)