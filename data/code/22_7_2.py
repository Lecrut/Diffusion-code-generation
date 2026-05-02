def check_odd_even(number):
    remainder = number % 2
    if remainder == 0:
        return "Even"
    else:
        return "Odd"
if __name__ == '__main__':
    sample_numbers = [4, 7, 10, 15, 22]
    for num in sample_numbers:
        result = check_odd_even(num)
        print(f"Number: {num}, Remainder when divided by 2: {num % 2}, Classification: {result}")