def filter_divisible_by_three(numbers):
    return list(filter(lambda x: x % 3 == 0, numbers))

if __name__ == '__main__':
    sample_values = [12, 15, 18, 20, 21, 24]
    result = filter_divisible_by_three(sample_values)
    print(result)