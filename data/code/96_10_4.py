if __name__ == '__main__':
    a = True
    b = False
    c = True
    result = not a or (b and c) and a
    print(result)