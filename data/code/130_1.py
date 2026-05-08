import sys
def check_zero(number):
    if number == 0:
        return True
    else:
        return False
if __name__ == '__main__':
    sample_values = [0, 5, -3, 0.0]
    for value in sample_values:
        result = check_zero(value)
        print(f"Checking value: {value}, Is zero: {result}")