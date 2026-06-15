import sys
def find_smallest(input_line):
    try:
        numbers = input_line.split()
        if not numbers:
            return None
        integers = [int(x) for x in numbers]
        return min(integers)
    except ValueError:
        return "Error: Input contains non-integer values."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    sample_input = "10 -5 22 3 -100 1"
    result = find_smallest(sample_input)
    print(result)