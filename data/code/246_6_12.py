import sys

def calculate_total(a, b):
    return a + b

if __name__ == '__main__':
    A = 10
    B = 25
    total = calculate_total(A, B)
    sys.stdout.write(str(total))