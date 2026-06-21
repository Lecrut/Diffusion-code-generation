def is_odd(number):
    return number % 2 != 0

def filter_odd_numbers(iterable):
    if not isinstance(iterable, (list, tuple)):
        raise ValueError("Input must be an iterable of numbers")
    
    return list(filter(is_odd, iterable))

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filter_odd_numbers(sample_values))