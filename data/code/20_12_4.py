def check_even(number: int) -> bool:
    remainder = number % 2
    if remainder == 0:
        return True
    return False

if __name__ == '__main__':
    sample_numbers = [0, 1, 2, 3, 4, 5, -1, -2, -3, 100]
    for num in sample_numbers:
        print(check_even(num))