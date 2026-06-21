EVEN_THRESHOLD = 2

def is_even(number):
    return number % EVEN_THRESHOLD == 0

def filter_evens(numbers):
    return list(filter(is_even, numbers))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_evens(sample_list)
    print(result)