import sys
NUM1 = 42
NUM2 = 7

def calculate_sum(x, y):
    return x + y
if __name__ == '__main__':
    result = calculate_sum(NUM1, NUM2)
    sys.stdout.write(str(result))