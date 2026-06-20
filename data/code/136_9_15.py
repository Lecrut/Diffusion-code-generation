def is_divisible_by_three_or_five(n: int) -> bool:
    return n % 3 == 0 or n % 5 == 0

def transform_numbers(numbers):
    return (x * 2 for x in numbers if is_divisible_by_three_or_five(x))

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = transform_numbers(sample_numbers)
    print(list(result))