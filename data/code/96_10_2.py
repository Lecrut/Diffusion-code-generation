if __name__ == '__main__':
    a = True
    b = False
    c = True
    d = False
    result = not a or (b and c) and d
    print(result)