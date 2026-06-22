EVEN_NUMBER_THRESHOLD = 2

def filter_even_numbers(integer_list):
    even_numbers = [num for num in integer_list if num % EVEN_NUMBER_THRESHOLD == 0]
    return even_numbers

if __name__ == '__main__':
    sample_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_even_numbers(sample_integers)
    print(result)