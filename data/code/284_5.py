def reverse_iterable(input_iterable):
    for item in reversed(list(input_iterable)):
        yield item
if __name__ == '__main__':
    sample = [1, 2, 3, 4, 5]
    reversed_result = list(reverse_iterable(sample))
    print(reversed_result)