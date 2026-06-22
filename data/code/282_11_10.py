def validate_input(input_data):
    try:
        numbers = [int(item) for item in input_data.split()]
        return numbers
    except ValueError:
        raise ValueError("Error: Invalid input detected.")

def calculate_total(numbers):
    try:
        return sum(numbers)
    except TypeError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_input = "10 20 30 40 50"
    numbers = validate_input(sample_input)
    result = calculate_total(numbers)
    print(result)