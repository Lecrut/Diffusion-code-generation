def positive_filter(numbers):
    for number in numbers:
        if number > 0:
            yield True

if __name__ == '__main__':
    sample_values = [3, -1, 2, 0, -5, 8]
    result = list(positive_filter(sample_values))
    print(result)