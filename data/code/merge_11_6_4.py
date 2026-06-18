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
    sample_list = [2, 4, 6, 8]
    result = calculate_stats(sample_list)
    print(result)