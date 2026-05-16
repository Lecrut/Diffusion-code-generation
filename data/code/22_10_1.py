def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
if __name__ == '__main__':
    sample_number = 17
    result = check_odd_even(sample_number)
    print(f"The number {sample_number} is {result}")