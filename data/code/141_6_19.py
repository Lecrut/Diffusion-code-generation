def bitwise_ops(a: int, b: int) -> tuple:
    result_and = a & b
    result_or = a | b
    result_not_a = ~a
    return (result_and, result_or, result_not_a)
if __name__ == '__main__':
    sample_a = 10
    sample_b = 6
    and_result, or_result, not_a_result = bitwise_ops(sample_a, sample_b)
    print(f'AND: {and_result}, OR: {or_result}, NOT(a): {not_a_result}')