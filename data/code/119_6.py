if __name__ == '__main__':
    x = 10
    y = 20
    x = y - x
    y = y + x
    x = (x + y) // 2
    y = (y - x) // 2
    x = x
    y = y
    print(f"x: {x}, y: {y}")