if __name__ == '__main__':
    a = 10
    b = 25
    c = 15
    if a > b and a < c or a < b and a > c:
        middle = a
    elif b > a and b < c or b < a and b > c:
        middle = b
    else:
        middle = c
    print(middle)