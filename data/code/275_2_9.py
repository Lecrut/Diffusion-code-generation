def calculate_product(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

if __name__ == '__main__':
    sample_numbers = (2, 3, 4)
    result = calculate_product(sample_numbers)
    print(result)