def short_circuit_evaluation():
    conditions = {
        'A': True,
        'B': False,
        'C': True
    }
    result_and = conditions['A'] and conditions['B']
    result_or = conditions['A'] or conditions['B']
    return (result_and, result_or)

if __name__ == '__main__':
    and_result, or_result = short_circuit_evaluation()
    print(f'AND Result: {and_result}')
    print(f'OR Result: {or_result}')