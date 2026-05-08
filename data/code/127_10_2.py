import sys
def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
if __name__ == '__main__':
    sample_numbers = [10, 7, 0, -4, 15]
    for num in sample_numbers:
        result = check_odd_even(num)
        print(f"The number {num} is {result}")