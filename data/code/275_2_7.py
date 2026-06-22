def multiply_elements(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

if __name__ == '__main__':
    sample_data = (5, 6, 7)
    result = multiply_elements(sample_data)
    print(result)