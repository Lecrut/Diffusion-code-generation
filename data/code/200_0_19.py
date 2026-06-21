def filter_even_numbers(int_list):
    return [num for num in int_list if num % 2 == 0]

if __name__ == '__main__':
    sample_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_even_numbers(sample_integers)
    print(result)