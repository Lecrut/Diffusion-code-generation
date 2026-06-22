def multiply_elements(num_tuple):
    product = 1
    for num in num_tuple:
        product *= num
    return product

if __name__ == '__main__':
    sample_data = (5, 6, 7)
    result = multiply_elements(sample_data)
    print(result)