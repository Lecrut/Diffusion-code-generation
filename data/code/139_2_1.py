def logic_operations(A, B, C):
    and_result = A and B and C
    or_result = A or B or C
    not_A = not A
    not_B = not B
    not_C = not C
    return {
        "AND": and_result,
        "OR": or_result,
        "NOT_A": not_A,
        "NOT_B": not_B,
        "NOT_C": not_C
    }
if __name__ == '__main__':
    sample_A = True
    sample_B = False
    sample_C = True
    results = logic_operations(sample_A, sample_B, sample_C)
    print(results)