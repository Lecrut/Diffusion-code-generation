def perform_basic_operations(data):
    if len(data) < 2:
        return "Error: List must contain at least two elements"
    num1 = data[0]
    num2 = data[1]
    result = {}
    result['num1'] = num1
    result['num2'] = num2
    result['sum'] = num1 + num2
    result['difference'] = num1 - num2
    result['product'] = num1 * num2
    result['quotient'] = num1 / num2 if num2 != 0 else "Undefined (Division by zero)"
    return result
if __name__ == '__main__':
    sample_list = [10, 5]
    results = perform_basic_operations(sample_list)
    print(results)
    sample_list_2 = [20, 4]
    results_2 = perform_basic_operations(sample_list_2)
    print(results_2)