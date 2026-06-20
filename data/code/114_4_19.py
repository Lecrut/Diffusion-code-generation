if __name__ == '__main__':
    factor_a = 25
    factor_b = 4
    if not isinstance(factor_a, (int, float)) or not isinstance(factor_b, (int, float)):
        raise ValueError("Both factors must be numbers")
    product = factor_a * factor_b
    print(product)