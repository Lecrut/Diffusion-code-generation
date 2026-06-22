CONVERSION_FACTOR = 1

def compare_quantities(quantity1, quantity2):
    return quantity1 == quantity2 * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_quantity1 = 5
    sample_quantity2 = 5
    result = compare_quantities(sample_quantity1, sample_quantity2)
    print(result)