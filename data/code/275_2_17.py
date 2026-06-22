def calculate_product(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

if __name__ == '__main__':
    sample_values = (5, 6, 7)
    result = calculate_product(sample_values)
    print(result)