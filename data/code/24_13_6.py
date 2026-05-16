import sys
def check_number(number):
    if number < 0:
        print("The entered number is negative.")
    else:
        print("The entered number is not negative.")
if __name__ == '__main__':
    sample_values = [10, -5, 0, 3.14, -100]
    for value in sample_values:
        if isinstance(value, int):
            check_number(value)
        else:
            print(f"Skipping non-integer input: {value}")