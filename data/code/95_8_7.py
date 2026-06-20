def is_positive_even_and_less_than_100(number):
    if number > 0 and number % 2 == 0 and number < 100:
        return True
    else:
        return False

if __name__ == '__main__':
    sample_numbers = [42, -5, 102, 8]
    for num in sample_numbers:
        result = is_positive_even_and_less_than_100(num)
        print(f"Number {num}: {'is' if result else 'is not'} positive, even, and less than 100")