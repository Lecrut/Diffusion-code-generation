def is_valid_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def calculate_sum(input_data):
    total = 0
    for value in input_data:
        if is_valid_integer(value):
            total += int(value)
        else:
            print(f"Error: Invalid input '{value}' found. Skipping.")
    return total

if __name__ == '__main__':
    sample_input = [
        "10",
        "25",
        "hello",
        "30",
        "-5"
    ]
    result = calculate_sum(sample_input)
    print(result)