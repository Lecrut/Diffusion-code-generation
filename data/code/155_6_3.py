def calculate_sum(input_string):
    numbers = input_string.split()
    total = 0
    for item in numbers:
        try:
            total += int(item)
        except ValueError:
            print(f"Error: '{item}' is not a valid integer.")
            return None
    return total
if __name__ == '__main__':
    sample_input = "10 25 30 45"
    result = calculate_sum(sample_input)
    if result is not None:
        print(result)