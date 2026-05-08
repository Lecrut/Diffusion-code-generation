import sys
def reverse_integers():
    try:
        data = sys.stdin.read().split()
        if len(data) < 2:
            return
        a = int(data[0])
        b = int(data[1])
        reversed_result = f"{b} {a}"
        print(reversed_result)
    except ValueError:
        print("Error: Invalid input. Please provide two integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    sample_a = 123
    sample_b = 456
    try:
        reversed_result = f"{sample_b} {sample_a}"
        print(reversed_result)
    except Exception:
        print("Error processing sample values.")