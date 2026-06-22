def is_numeric(value):
    return isinstance(value, (int, float))

def filter_divisible_by_three(numbers):
    if not all(is_numeric(x) for x in numbers):
        raise ValueError("All elements must be numeric.")
    return list(filter(lambda x: x % 3 == 0, numbers))

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_divisible_by_three(sample_values)
    print(result)