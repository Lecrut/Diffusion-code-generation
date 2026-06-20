if __name__ == '__main__':
    x = 10
    y = 20
    while x != 0:
        temp = x
        x = y - (y // x) * x
        y = temp
    print(f"x: {x}, y: {y}")