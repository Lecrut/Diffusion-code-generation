def order_pair(a, b):
    if a < b:
        return a, b
    else:
        return b, a

if __name__ == '__main__':
    print(order_pair(5, 3))
    print(order_pair(10, 20))
    print(order_pair(0, 0))