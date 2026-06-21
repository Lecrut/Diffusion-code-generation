def is_odd(number):
    return number % 2 != 0

def filter_odds(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, int) for num in numbers):
        raise ValueError("Input must be a list of integers")
    
    return [num for num in numbers if is_odd(num)]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_odds(sample_list)
    print(result)