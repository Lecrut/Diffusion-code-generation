from decimal import Decimal

def validate_inputs(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numbers")
    return True

def perform_operations(a, b):
    validate_inputs(a, b)
    
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    quotient_result = Decimal(a) / Decimal(b) if b != 0 else None
    
    return {
        'sum': sum_result,
        'difference': difference_result,
        'product': product_result,
        'quotient': quotient_result
    }

if __name__ == '__main__':
    sample_values1 = (20, 4)
    results1 = perform_operations(*sample_values1)
    print(results1)
    
    sample_values2 = (5, 3)
    results2 = perform_operations(*sample_values2)
    print(results2)