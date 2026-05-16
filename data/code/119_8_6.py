import sys
def reverse_integers():
    try:
        line = sys.stdin.read().strip()
        if not line:
            return
        parts = line.split()
        if len(parts) != 2:
            raise ValueError("Expected exactly two integers.")
        num1 = int(parts[0])
        num2 = int(parts[1])
        reversed_result = f"{num2}, {num1}"
        print(reversed_result)
    except ValueError:
        print("Error: Invalid input. Please provide two integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    sample_num1 = 123
    sample_num2 = 456
    reversed_result = f"{sample_num2}, {sample_num1}"
    print(reversed_result)