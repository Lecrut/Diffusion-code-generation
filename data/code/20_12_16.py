def is_even(number):
    remainder = number % 2
    is_even_flag = remainder == 0
    return is_even_flag

if __name__ == '__main__':
    samples = [10, 13, 0, -5, -8, 100]
    results = [is_even(num) for num in samples]
    for result in results:
        print(result)