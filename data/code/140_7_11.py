def positive_numbers(numbers):
    for number in numbers:
        if number > 0:
            yield number

if __name__ == '__main__':
    sample_tuple = (1, -2, 3, -4, 5)
    result = list(positive_numbers(sample_tuple))
    print(result)