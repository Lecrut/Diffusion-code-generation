def filter_transform_numbers(numbers):
    return (x * 2 for x in numbers if x % 3 == 0 or x % 5 == 0)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_transform_numbers(sample_values)
    print(list(result))