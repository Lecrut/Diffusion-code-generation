def calculate_sum(input_string):
    try:
        numbers = input_string.split()
        total = 0
        for item in numbers:
            total += int(item)
        return total
    except ValueError:
        return "Error: Invalid input. Please ensure all parts are integers."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    sample_input = "10 20 35 5"
    result = calculate_sum(sample_input)
    print(result)