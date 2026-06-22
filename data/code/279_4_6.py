MUL_FACTOR = 2

def cycle_and_double(numbers):
    for number in numbers:
        print(number * MUL_FACTOR)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    cycle_and_double(sample_values)