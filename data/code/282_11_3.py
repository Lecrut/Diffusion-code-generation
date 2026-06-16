import sys
if __name__ == '__main__':
    input_data = "10 20 30 40 50"
    numbers = []
    try:
        input_numbers = input_data.split()
        for item in input_numbers:
            numbers.append(int(item))
        total_sum = sum(numbers)
        print(total_sum)
    except ValueError:
        sys.stderr.write("Error: Invalid input detected.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")