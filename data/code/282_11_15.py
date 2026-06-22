def validate_input(input_data):
    try:
        return [int(item) for item in input_data.split()]
    except ValueError:
        raise ValueError("Error: Invalid input detected.")

def calculate_total(numbers):
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = "10 20 30 40 50"
    try:
        validated_numbers = validate_input(sample_numbers)
        total_sum = calculate_total(validated_numbers)
        print(total_sum)
    except ValueError as e:
        print(e)