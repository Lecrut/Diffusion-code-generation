def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

if __name__ == '__main__':
    x, y = 5, 10
    print(swap(x, y))