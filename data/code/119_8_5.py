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
        print("Error: Input must be two integers.")
    except Exception:
        print("An unexpected error occurred.")
if __name__ == '__main__':
    a = 123
    b = 456
    reversed_result = f"{b} {a}"
    print(reversed_result)