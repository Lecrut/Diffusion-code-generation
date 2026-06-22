def positive_filter(numbers):
    for number in numbers:
        if number > 0:
            yield True

if __name__ == '__main__':
    sample_values = [-10, 5, -3, 8, 0, -1, 7]
    result = list(positive_filter(sample_values))
    print(result)