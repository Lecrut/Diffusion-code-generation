import sys
def calculate_product(numbers):
    product = 1
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("List contains non-numeric elements")
        product *= num
    return product
if __name__ == '__main__':
    sample_input = "2 3 4 5"
    try:
        input_numbers = [float(x) for x in sample_input.split()]
        result = calculate_product(input_numbers)
        print(result)
    except ValueError as e:
        print(f"Error: Invalid input format. {e}", file=sys.stderr)
    except TypeError as e:
        print(f"Error: Data type issue. {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)