EVEN_THRESHOLD = 2

def filter_even_numbers(numbers):
    return [num for num in numbers if num % EVEN_THRESHOLD == 0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = filter_even_numbers(sample_list)
    print(even_numbers)