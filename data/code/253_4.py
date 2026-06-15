if __name__ == '__main__':
    a = 10
    b = 5
    c = 20
    if a > b and a < c or a < b and a > c:
        middle = a
    elif b > a and b < c or b < a and b > c:
        middle = b
    else:
        middle = c
    print(middle)