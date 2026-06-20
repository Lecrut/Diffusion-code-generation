def reverse_order(a: float, b: float) -> (float, float):
    temp = a
    a = b
    b = temp
    return a, b

if __name__ == '__main__':
    x = 1.414
    y = 2.718
    result = reverse_order(x, y)
    print(result)