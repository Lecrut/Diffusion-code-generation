if __name__ == '__main__':
    x = 5 if True else -3
    result = bool(x > 0)
    print(result, "x =", x)