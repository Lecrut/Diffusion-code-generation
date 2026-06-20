if __name__ == '__main__':
    A_TRUE = True
    B_FALSE = False
    result = (A_TRUE and not B_FALSE) or (not A_TRUE and B_FALSE)
    print(result)