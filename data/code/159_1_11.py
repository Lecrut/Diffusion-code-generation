def is_odd(number):
    return number % 2 != 0

def filter_odds(numbers):
    return [num for num in numbers if is_odd(num)]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_numbers = filter_odds(sample_values)
    print(odd_numbers)