from decimal import Decimal, getcontext

def perform_operations(a, b):
    getcontext().prec = 10
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    quotient_result = a / b if b != 0 else Decimal('Infinity')
    return {'sum': sum_result, 'difference': difference_result, 'product': product_result, 'quotient': quotient_result}
if __name__ == '__main__':
    sample_values = [20, 4]
    results = perform_operations(*sample_values)
    print(results)