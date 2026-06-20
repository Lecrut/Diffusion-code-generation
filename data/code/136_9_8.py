def is_divisible_by_3_or_5(x):
    return x % 3 == 0 or x % 5 == 0

def filter_transform(numbers):
    return (x * 2 for x in numbers if is_divisible_by_3_or_5(x))

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_transform(sample_numbers)
    print(list(result))