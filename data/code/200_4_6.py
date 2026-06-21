def product_of_first_elements(tuples_list):
    return prod(item[0] for item in tuples_list)

if __name__ == '__main__':
    sample_data = [(2, 3), (4, 5), (6, 7)]
    print(product_of_first_elements(sample_data))