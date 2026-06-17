if __name__ == '__main__':
    x, y, z = 10, 5, 20
    middle = (x + y + z) // 3 if sorted((x, y, z))[1] == y else (x + y + z) // 3 if sorted((x, y, z))[1] == x else (x + y + z) // 3
    print(middle)