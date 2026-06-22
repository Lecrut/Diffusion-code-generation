def order_numbers(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

if __name__ == '__main__':
    print(order_numbers(3.14, 2.71, 1.61))