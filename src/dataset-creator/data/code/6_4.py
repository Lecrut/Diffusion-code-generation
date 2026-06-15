def calculate_product(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product
if __name__ == '__main__':
    sample_list = [2, 3, 5, 10]
    result = calculate_product(sample_list)
    print(result)