def perform_operations(data):
    if len(data) < 2:
        return "Error: List must contain at least two elements"
    a = data[0]
    b = data[1]
    result = {}
    result['a'] = a
    result['b'] = b
    result['sum'] = a + b
    result['difference'] = a - b
    result['product'] = a * b
    result['quotient'] = a / b if b != 0 else "Undefined (Division by zero)"
    return result
if __name__ == '__main__':
    sample_list = [10, 5]
    operations_result = perform_operations(sample_list)
    print(operations_result)
    sample_list_2 = [20, 4]
    operations_result_2 = perform_operations(sample_list_2)
    print(operations_result_2)