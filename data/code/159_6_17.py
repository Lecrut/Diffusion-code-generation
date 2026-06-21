def odd_numbers(numbers):
    for number in numbers:
        if number % 2 != 0:
            yield number

if __name__ == '__main__':
    sample_list = [10, 15, 20, 25, 30, 35]
    for odd in odd_numbers(sample_list):
        print(odd)