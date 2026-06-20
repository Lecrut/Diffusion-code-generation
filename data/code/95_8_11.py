MAX_VALUE = 100

def is_positive_even_and_under_limit(number):
    return number > 0 and number % 2 == 0 and number < MAX_VALUE

if __name__ == '__main__':
    sample_values = [3, 5, 8, 99, 100, -2, 1.5]
    for value in sample_values:
        result = is_positive_even_and_under_limit(value)
        print(f"Number {value}: {'is' if result else 'is not'} positive, even, and less than {MAX_VALUE}.")