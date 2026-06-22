import sys
A = 5
B = 10

def calculate_sum(a, b):
    return a + b
if __name__ == '__main__':
    try:
        result = calculate_sum(A, B)
        sys.stdout.write(str(result))
    except Exception as e:
        sys.stderr.write(f'Error: {e}')