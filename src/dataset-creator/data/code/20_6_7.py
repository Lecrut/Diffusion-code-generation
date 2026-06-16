def filter_positive(numbers):
    return (n for n in numbers if n >= 0)
if __name__ == '__main__':
    data = [10, -5, 3, -20, 8, 0, -1]
    positive_gen = filter_positive(data)
    result = list(positive_gen)
    print(result)