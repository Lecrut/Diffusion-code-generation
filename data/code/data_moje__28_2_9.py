def order_numbers(a, b):
    if a < b:
        return a, b
    else:
        return b, a

if __name__ == '__main__':
    val1 = 10
    val2 = 5
    result = order_numbers(val1, val2)
    print(result)