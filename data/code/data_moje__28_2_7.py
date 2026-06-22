def order_numbers(a, b):
    if a <= b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    print(order_numbers(5, 3))
    print(order_numbers(10, 20))
    print(order_numbers(-1, -5))