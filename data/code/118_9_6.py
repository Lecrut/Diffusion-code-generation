def multiply_numbers(a, b):
    return a * b

if __name__ == '__main__':
    factor1 = 20
    factor2 = 3
    if isinstance(factor1, (int, float)) and isinstance(factor2, (int, float)):
        product = multiply_numbers(factor1, factor2)
        print(f"The result of multiplying {factor1} and {factor2} is: {product}")
    else:
        print("Error: Both inputs must be valid numbers.")