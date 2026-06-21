def order_two(a, b):
    if a <= b:
        return (a, b)
    return (b, a)

if __name__ == '__main__':
    print(order_two(3, 5))
    print(order_two(10, 2))