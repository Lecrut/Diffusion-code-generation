import sys
if __name__ == '__main__':
    input_data = "10 5 20 3 15"
    try:
        numbers = list(map(int, input_data.split()))
        if numbers:
            minimum = min(numbers)
            print(minimum)
        else:
            print("Input list is empty.")
    except ValueError:
        print("Error: Input contains non-integer values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")