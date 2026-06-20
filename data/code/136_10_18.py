def evaluate_logical_operators(a, b):
    AND_RESULT = a and b
    OR_RESULT = a or b
    NOT_A_RESULT = not a
    return (AND_RESULT, OR_RESULT, NOT_A_RESULT)
if __name__ == '__main__':
    A = True
    B = False
    and_result, or_result, not_a_result = evaluate_logical_operators(A, B)
    print(f'a: {A}, b: {B}')
    print(f'a AND b: {and_result}')
    print(f'a OR b: {or_result}')
    print(f'NOT a: {not_a_result}')