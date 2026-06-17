import sys
if __name__ == '__main__':
    input_data = "10 25 33 48 50"
    numbers = []
    try:
        for item in input_data.split():
            numbers.append(int(item))
        total_count = len(numbers)
        print(total_count)
    except ValueError:
        sys.stderr.write("Error: Input contained non-integer values.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")