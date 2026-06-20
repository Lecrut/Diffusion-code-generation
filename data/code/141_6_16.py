def bitwise_operations(a: int, b: int) -> tuple:
    result_and = a & b
    result_or = a | b
    result_not_a = ~a
    return result_and, result_or, result_not_a

if __name__ == '__main__':
    sample_values = (10, 5)
    and_result, or_result, not_a_result = bitwise_operations(*sample_values)
    print(f"AND: {and_result}, OR: {or_result}, NOT(a): {not_a_result}")