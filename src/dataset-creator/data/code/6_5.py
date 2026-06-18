def calculate_cumulative_product(numbers):
    cumulative_product = 1
    for num in numbers:
        cumulative_product *= num
    return cumulative_product
if __name__ == '__main__':
    sample_inputs = [2, 3, 4, 5]
    result = calculate_cumulative_product(sample_inputs)
    print(result)