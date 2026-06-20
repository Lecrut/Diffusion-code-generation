def short_circuit_evaluation():
    a = True
    b = False
    result_and = a and b
    result_or = a or b
    result_not_a = not a
    return (result_and, result_or, result_not_a)
if __name__ == '__main__':
    and_result, or_result, not_a_result = short_circuit_evaluation()
    print(f'AND: {and_result}, OR: {or_result}, NOT A: {not_a_result}')