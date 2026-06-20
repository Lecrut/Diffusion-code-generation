def short_circuit_evaluation():
    a = True
    b = False
    result_and = a and b
    result_or = a or b
    result_not = not a
    return (result_and, result_or, result_not)
if __name__ == '__main__':
    and_result, or_result, not_result = short_circuit_evaluation()
    print(f'and: {and_result}, or: {or_result}, not: {not_result}')