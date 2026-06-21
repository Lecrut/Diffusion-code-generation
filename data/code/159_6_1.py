def odd_numbers(numbers):
    for number in numbers:
        if number % 2 != 0:
            yield number

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for odd in odd_numbers(sample_list):
        print(odd)