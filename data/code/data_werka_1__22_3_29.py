def is_odd(number):
    return isinstance(number, int) and number % 2 != 0

def filter_odds(numbers):
    return [num for num in numbers if is_odd(num)]

if __name__ == '__main__':
    sample_values = [17, 4, 9, 15, 22, 3]
    odd_numbers = filter_odds(sample_values)
    print(odd_numbers)