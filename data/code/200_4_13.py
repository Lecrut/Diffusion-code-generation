def product_first_elements(data):
    product = 1
    for item in data:
        if not item:
            continue
        product *= item[0]
    return product

if __name__ == '__main__':
    sample_data = [(2, 3), (4, 5), (6, 7)]
    result = product_first_elements(sample_data)
    print(result)