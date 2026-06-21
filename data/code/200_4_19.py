def product_of_first_elements(tuples_list):
    return prod(x for x, _ in tuples_list)

if __name__ == '__main__':
    sample_tuples = [(2, 3), (4, 5), (6, 7)]
    print(product_of_first_elements(sample_tuples))