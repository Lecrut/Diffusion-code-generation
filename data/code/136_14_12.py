def short_circuit_evaluation():
    a = True
    b = False
    result_and = a and b
    result_or = a or b
    return (result_and, result_or)
if __name__ == '__main__':
    and_result, or_result = short_circuit_evaluation()
    print('AND Result:', and_result)
    print('OR Result:', or_result)