import sys

NUM1 = 10
NUM2 = 25

def calculate_total(a, b):
    return a + b

if __name__ == '__main__':
    total = calculate_total(NUM1, NUM2)
    sys.stdout.write(str(total))