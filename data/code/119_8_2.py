def reverse_integers():
    try:
        line = input()
        parts = line.split()
        if len(parts) != 2:
            raise ValueError("Input must contain exactly two integers.")
        num1 = int(parts[0])
        num2 = int(parts[1])
        reversed_result = f"{num2}, {num1}"
        print(reversed_result)
    except ValueError as e:
        print(f"Error: Invalid input. Please ensure both inputs are integers. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    sample_input = "123 456"
    try:
        parts = sample_input.split()
        if len(parts) == 2:
            a = int(parts[0])
            b = int(parts[1])
            reversed_result = f"{b}, {a}"
            print(reversed_result)
        else:
            print("Sample input format error.")
    except ValueError:
        print("Sample input contained non-integer values.")