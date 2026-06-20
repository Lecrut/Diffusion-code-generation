PRODUCT_FACTOR_1 = 0.1
PRODUCT_FACTOR_2 = 0.2

def calculate_product(factor1: float, factor2: float) -> float:
    return factor1 * factor2

if __name__ == '__main__':
    result = calculate_product(PRODUCT_FACTOR_1, PRODUCT_FACTOR_2)
    print(result)