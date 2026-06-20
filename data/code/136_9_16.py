def filter_transform(numbers):
    return (x * 3 if x % 2 == 0 else -x for x in numbers if x % 7 != 0)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_transform(sample_numbers)
    print(list(result))