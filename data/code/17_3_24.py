EVEN_CHECK = lambda x: x % 2 == 0

def filter_even_numbers(numbers):
    return [num for num in numbers if EVEN_CHECK(num)]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = filter_even_numbers(sample_values)
    print(even_numbers)