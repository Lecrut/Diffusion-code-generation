if __name__ == '__main__':
    X = True
    Y = False
    Z = True
    W = False
    expression = "(X and Y) or (Z and not W)"
    result = (X and Y) or (Z and not W)
    print(result)