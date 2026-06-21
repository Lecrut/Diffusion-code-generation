def product_of_first_elements(tuples_list):
    return reduce(lambda x, y: x * y[0], tuples_list, 1)

if __name__ == '__main__':
    sample_tuples = [(2, 'a'), (3, 'b'), (4, 'c')]
    print(product_of_first_elements(sample_tuples))