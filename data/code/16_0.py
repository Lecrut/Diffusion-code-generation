import sys
def check_positivity(number):
    if number > 0:
        return True
    else:
        return False
if __name__ == '__main__':
    sample_numbers = [10, -5, 0, 3.14, -100]
    for num in sample_numbers:
        if isinstance(num, (int, float)):
            result = check_positivity(num)
            print(f"Number: {num}, Is Positive: {result}")
        else:
            print(f"Skipping invalid input: {num}")