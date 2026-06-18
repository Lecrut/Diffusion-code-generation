def calculate_sequential_products(numbers):
    if len(numbers) < 2:
        return 0
    total_sum = 0
    for i in range(len(numbers) - 1):
        product = numbers[i] * numbers[i+1]
        total_sum += product
    return total_sum
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4]
    result = calculate_sequential_products(sample_list)
    print(result)