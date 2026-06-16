def product_of_list(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product
if __name__ == '__main__':
    sample_list = [2, 3, 5, 10]
    result = product_of_list(sample_list)
    print(result)