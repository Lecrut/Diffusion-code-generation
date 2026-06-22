import sys
NUMBER_ONE = 20
NUMBER_TWO = 35

def add_numbers(a, b):
    return a + b
if __name__ == '__main__':
    sample_num1 = NUMBER_ONE
    sample_num2 = NUMBER_TWO
    combined_sum = add_numbers(sample_num1, sample_num2)
    sys.stdout.write(str(combined_sum))