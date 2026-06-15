import sys
def find_largest(input_line):
    if not input_line:
        return None
    try:
        numbers = input_line.split()
        if not numbers:
            return None
        nums = [int(n) for n in numbers]
        return max(nums)
    except ValueError:
        return "Error: Invalid input detected"
    except Exception:
        return "Error: An unexpected error occurred"
if __name__ == '__main__':
    sample_input = "10 5 22 8 30"
    result = find_largest(sample_input)
    print(result)