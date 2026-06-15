import sys
def find_smallest(input_line):
    try:
        numbers = input_line.split()
        if not numbers:
            return None
        integers = [int(n) for n in numbers]
        return min(integers)
    except ValueError:
        return "Error: Non-integer input found."
    except Exception:
        return "An unexpected error occurred."
if __name__ == '__main__':
    sample_input = "10 5 22 3 8"
    result = find_smallest(sample_input)
    print(result)