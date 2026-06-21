def product_of_first_elements(tuples_list):
    product = 1
    for first_element, _ in tuples_list:
        product *= first_element
    return product

if __name__ == '__main__':
    sample_tuples = [(2, 3), (4, 5), (6, 7)]
    print(product_of_first_elements(sample_tuples))