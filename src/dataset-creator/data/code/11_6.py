def calculate_stats(numbers):
    if not numbers:
        return (0, 0, None, None)
    total_sum = sum(numbers)
    total_product = 1
    minimum = numbers[0]
    maximum = numbers[0]
    for num in numbers:
        total_product *= num
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    return (total_sum, total_product, minimum, maximum)
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    result = calculate_stats(sample_list)
    print(result)