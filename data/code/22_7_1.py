def check_odd_even(number):
    remainder = number % 2
    if remainder == 0:
        return "Even"
    else:
        return "Odd"
if __name__ == '__main__':
    sample_numbers = [10, 7, 4, 1, 0, -3]
    for num in sample_numbers:
        result = check_odd_even(num)
        print(f"The number {num} is {result}")