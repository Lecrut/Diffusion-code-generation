import sys
def find_largest(input_line):
    if not input_line.strip():
        return None
    try:
        numbers = [float(x) for x in input_line.split()]
        if not numbers:
            return None
        return max(numbers)
    except ValueError:
        return "Error: Invalid input detected"
if __name__ == '__main__':
    sample_input = "10 5 22 8 30"
    result = find_largest(sample_input)
    print(result)