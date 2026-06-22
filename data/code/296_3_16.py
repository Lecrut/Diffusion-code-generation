GEOMETRIC_SEQUENCE_FORMULA = lambda first_term, common_ratio, n: first_term * common_ratio ** (n - 1)

def calculate_nth_term(first_term, common_ratio, n):
    return GEOMETRIC_SEQUENCE_FORMULA(first_term, common_ratio, n)
if __name__ == '__main__':
    print(calculate_nth_term(2, 3, 4))