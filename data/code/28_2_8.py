def order_pair(a, b):
    return (a, b) if a < b else (b, a)

if __name__ == '__main__':
    result = order_pair(5, 3)
    print(result)