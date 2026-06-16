import sys
def calculate_sum(data):
    total = 0
    for item in data:
        if isinstance(item, int):
            total += item
        else:
            pass
    return total
if __name__ == '__main__':
    sample_input = "10 20 30 40 5"
    try:
        input_data = sample_input.split()
        numbers = []
        for item in input_data:
            numbers.append(int(item))
        result = calculate_sum(numbers)
        print(result)
    except ValueError:
        sys.stderr.write("Error: Input contains non-integer values.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")