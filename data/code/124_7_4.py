if __name__ == '__main__':
    x = 12
    y = 3
    
    sum_result = x + y
    difference_result = x - y
    product_result = x * y
    quotient_result = x / y if y != 0 else None
    modulus_result = x % y
    
    print(f"Sum: {sum_result}, Difference: {difference_result}, Product: {product_result}, Quotient: {quotient_result}, Modulus: {modulus_result}")