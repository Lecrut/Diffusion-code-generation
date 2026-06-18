def analyze_list(numbers):
    if not numbers:
        return (0, 0, None, None)
    total_sum = sum(numbers)
    total_product = 1
    for x in numbers:
        total_product *= x
    minimum = min(numbers)
    maximum = max(numbers)
    return (total_sum, total_product, minimum, maximum)
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    result = analyze_list(sample_list)
    print(result)