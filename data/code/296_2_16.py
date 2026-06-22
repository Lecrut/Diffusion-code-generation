def are_in_proportion(a, b, c, d):
    if b == 0 or d == 0:
        return False
    return a / b == c / d
if __name__ == '__main__':
    print(are_in_proportion(10, 4, 5, 2))
    print(are_in_proportion(9, 3, 6, 2))