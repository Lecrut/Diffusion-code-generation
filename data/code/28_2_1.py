def order_numbers(a, b):
    if a < b:
        return a, b
    return b, a

if __name__ == '__main__':
    result = order_numbers(15, 3)
    print(result)