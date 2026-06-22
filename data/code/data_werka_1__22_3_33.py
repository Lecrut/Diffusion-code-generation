def is_odd(number):
    return isinstance(number, int) and number % 2 != 0

def filter_odds(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")
    
    odd_numbers = []
    for num in numbers:
        if is_odd(num):
            odd_numbers.append(num)
    
    return odd_numbers

if __name__ == '__main__':
    sample_values = [10, 23, 45, 68, 97, 21]
    result = filter_odds(sample_values)
    print(result)