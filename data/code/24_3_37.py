def is_negative(number):
    return number < 0

def filter_negative_numbers(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")
    
    negative_numbers = []
    for num in numbers:
        if isinstance(num, int) and is_negative(num):
            negative_numbers.append(num)
    
    return negative_numbers

if __name__ == '__main__':
    sample_values = [10, -3, 25, -7, 0, -1, 8]
    negative_numbers = filter_negative_numbers(sample_values)
    print(negative_numbers)