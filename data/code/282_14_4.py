import sys
def calculate_sum(input_string):
    numbers = []
    try:
        for item in input_string.split(','):
            if item.strip():
                numbers.append(float(item.strip()))
        return sum(numbers)
    except ValueError:
        return "Error: Invalid input. Please ensure all parts are valid numbers."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    sample_input = "10,5.5,20,3.14"
    result = calculate_sum(sample_input)
    print(result)