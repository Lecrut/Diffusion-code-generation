def product_of_first_elements(tuples_list):
    product = 1
    for first_element, _ in tuples_list:
        product *= first_element
    return product

if __name__ == '__main__':
    sample_tuples = [(2, 'a'), (3, 'b'), (4, 'c')]
    print(product_of_first_elements(sample_tuples))