def calculate_product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

if __name__ == '__main__':
    sample_values = (2, 3, 4)
    product = calculate_product(sample_values)
    print(product)