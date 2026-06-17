if __name__ == '__main__':
    a = 10
    b = 25
    c = 15
    if (a <= b and b <= c) or (c <= b and b <= a):
        middle = b
    elif (b <= a and a <= c) or (c <= a and a <= b):
        middle = a
    else:
        middle = c
    print(middle)