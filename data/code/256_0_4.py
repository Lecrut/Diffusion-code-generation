import sys
if __name__ == '__main__':
    data_input = "10.5 3.2 -5.8 9.1 0.0"
    try:
        numbers = [float(x) for x in data_input.split()]
        if not numbers:
            print("Range: 0.0")
        else:
            minimum = min(numbers)
            maximum = max(numbers)
            data_range = maximum - minimum
            print(data_range)
    except ValueError:
        print("Error: Invalid input. Please ensure all inputs are valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")