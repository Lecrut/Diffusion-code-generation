if __name__ == '__main__':
    x, y, z = 10, 20, 30
    middle = (x + y + z) // 3 if sorted((x, y, z))[1] == y else (x + z) // 2 if x < z else (y + z) // 2
    print(middle)