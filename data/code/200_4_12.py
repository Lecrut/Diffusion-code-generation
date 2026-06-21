def product_of_first_elements(data):
    product = 1
    for item in data:
        if len(item) > 0:
            product *= item[0]
    return product

if __name__ == '__main__':
    sample_data = [(2, 3), (4, 5), (6, 7)]
    result = product_of_first_elements(sample_data)
    print(result)