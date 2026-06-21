def is_even(number):
    return number % 2 == 0

def filter_evens(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
        raise ValueError("Input must be a list of integers")
    
    evens = list(filter(is_even, numbers))
    return evens

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_evens(sample_list)
    print(result)