def evaluate_logical_operators():
    a = True
    b = False

    result_and = a and b
    result_or = a or b
    result_not_a = not a
    result_not_b = not b

    return result_and, result_or, result_not_a, result_not_b

if __name__ == '__main__':
    and_result, or_result, not_a_result, not_b_result = evaluate_logical_operators()
    print("a and b:", and_result)
    print("a or b:", or_result)
    print("not a:", not_a_result)
    print("not b:", not_b_result)