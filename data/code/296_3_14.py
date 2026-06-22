def nth_term_of_geometric_sequence(first_term, common_ratio, n):
    return first_term * common_ratio ** (n - 1)
if __name__ == '__main__':
    print(nth_term_of_geometric_sequence(2, 3, 4))