INITIAL_FACTOR = 1

def multiply_first_elements(data):
    product = INITIAL_FACTOR
    for item in data:
        product *= item[0]
    return product

if __name__ == '__main__':
    sample_data = [(2, 3), (4, 5), (6, 7)]
    result = multiply_first_elements(sample_data)
    print(result)