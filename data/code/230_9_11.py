def filter_divisible_by_three(numbers):
    return list(filter(lambda x: x % 3 == 0, numbers))

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_values = filter_divisible_by_three(sample_values)
    print(filtered_values)