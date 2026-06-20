def filter_transform(numbers):
    return (x * 2 if x % 3 == 0 else x for x in numbers if x % 5 != 0)

if __name__ == '__main__':
    sample_numbers = [10, 15, 20, 25, 30]
    result = filter_transform(sample_numbers)
    print(list(result))