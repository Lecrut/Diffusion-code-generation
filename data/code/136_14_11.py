def short_circuit_evaluation():
    a = True
    b = False
    result_and = a and b
    result_or = a or b
    return (result_and, result_or)
if __name__ == '__main__':
    and_result, or_result = short_circuit_evaluation()
    print(f'AND result: {and_result}, OR result: {or_result}')