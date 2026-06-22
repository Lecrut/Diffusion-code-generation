def calculate_geometric_term(first_term, common_ratio, term_number):
    return first_term * common_ratio ** (term_number - 1)
if __name__ == '__main__':
    first_term = 2
    common_ratio = 3
    term_number = 5
    result = calculate_geometric_term(first_term, common_ratio, term_number)
    print(result)