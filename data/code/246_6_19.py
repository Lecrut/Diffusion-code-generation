import sys
FIRST_NUMBER = 15
SECOND_NUMBER = 27

def compute_total(a, b):
    return a + b
if __name__ == '__main__':
    total = compute_total(FIRST_NUMBER, SECOND_NUMBER)
    sys.stdout.write(str(total))