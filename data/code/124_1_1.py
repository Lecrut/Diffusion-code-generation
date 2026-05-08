def perform_four_operations(a, b, c, d):
    sum_val = a + b + c + d
    difference = a - b
    product = a * b
    division_result = a / b
    return {
        "sum": sum_val,
        "difference": difference,
        "product": product,
        "division": division_result
    }
if __name__ == '__main__':
    result = perform_four_operations(10, 5, 3, 2)
    print(result)