def are_in_proportion(a, b, c, d):
    if b == 0 or d == 0:
        return False
    return (a / b) == (c / d)

if __name__ == '__main__':
    a = 10
    b = 4
    c = 5
    d = 2
    print(are_in_proportion(a, b, c, d))