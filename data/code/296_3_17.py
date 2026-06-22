def geometric_nth_term(first_term, common_ratio, n):
    return first_term * (common_ratio ** (n - 1))

if __name__ == '__main__':
    print(geometric_nth_term(2, 3, 5))