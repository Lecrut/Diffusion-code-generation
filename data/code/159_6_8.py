def odd_numbers(numbers):
    for number in numbers:
        if number % 2 != 0:
            yield number

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    odd_gen = odd_numbers(sample_list)
    for _ in range(len(sample_list)):
        print(next(odd_gen))