def calculate_stats(numbers):
    if not numbers:
        return (0, 0, None, None)
    total_sum = sum(numbers)
    product = 1
    for x in numbers:
        product *= x
    minimum = min(numbers)
    maximum = max(numbers)
    return (total_sum, product, minimum, maximum)
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    result = calculate_stats(sample_list)
    print(result)