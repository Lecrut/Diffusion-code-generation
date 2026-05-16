import sys
def check_zero(number):
    if number == 0:
        return True
    else:
        return False
if __name__ == '__main__':
    sample_numbers = [0, 5, -3, 0.0]
    for num in sample_numbers:
        result = check_zero(num)
        print(f"Checking {num}: {result}")