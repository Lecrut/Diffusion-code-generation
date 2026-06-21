def is_even(number):
    return number % 2 == 0

def filter_even_numbers(numbers):
    if not isinstance(numbers, list) or not all(isinstance(n, int) for n in numbers):
        raise ValueError("Input must be a list of integers")
    
    return list(filter(is_even, numbers))

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_even_numbers(sample_values)
    print(result)