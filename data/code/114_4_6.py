if __name__ == '__main__':
    factor_a = 5
    factor_b = 3
    if not (isinstance(factor_a, int) and isinstance(factor_b, int)):
        raise ValueError("Both factors must be integers.")
    result = factor_a * factor_b
    print(result)