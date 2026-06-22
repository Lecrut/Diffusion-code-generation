def are_in_proportion(a, b, c, d):
    return a * d == b * c
if __name__ == '__main__':
    print(are_in_proportion(2, 3, 4, 6))
    print(are_in_proportion(1, 2, 3, 5))