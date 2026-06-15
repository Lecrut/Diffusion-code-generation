if __name__ == '__main__':
    x, y, z = 10, 20, 30
    middle = (x + y + z) // 3 if x <= y <= z or x >= y >= z else max(min(x, y), min(y, z)) if x < y and y < z else min(max(x, y), max(y, z))
    print(middle)