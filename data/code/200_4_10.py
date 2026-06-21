def validate_data(data):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in data):
        raise ValueError("Data must be a list of tuples with exactly two elements each.")

def calculate_product_of_first_elements(data):
    product = 1
    for first_element, _ in data:
        product *= first_element
    return product

if __name__ == '__main__':
    sample_data = [(2, 'a'), (3, 'b'), (4, 'c')]
    validate_data(sample_data)
    result = calculate_product_of_first_elements(sample_data)
    print(result)