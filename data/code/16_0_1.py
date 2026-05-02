def check_positivity(number):
    if number > 0:
        return True
    else:
        return False
if __name__ == '__main__':
    sample_numbers = [10, -5, 0, 3.14, -100]
    for num in sample_numbers:
        if not isinstance(num, (int, float)):
            print(f"Error: Input '{num}' is not a valid number.")
            continue
        is_positive = check_positivity(num)
        print(f"The number {num} is positive: {is_positive}")