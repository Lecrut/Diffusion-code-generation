import sys
def find_largest(input_string):
    try:
        numbers = [int(x) for x in input_string.split()]
        if not numbers:
            return None
        return max(numbers)
    except ValueError:
        return "Error: Invalid input. Please ensure all inputs are valid integers."
if __name__ == '__main__':
    sample_input = "10 5 42 3 99 1"
    result = find_largest(sample_input)
    print(result)