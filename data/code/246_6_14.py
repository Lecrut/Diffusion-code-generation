import sys
NUM_ONE = 15
NUM_TWO = 27

def calculate_sum(a, b):
    return a + b
if __name__ == '__main__':
    result = calculate_sum(NUM_ONE, NUM_TWO)
    sys.stdout.write(str(result))