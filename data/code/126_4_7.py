def equal(a, b):
    if type(a) != type(b):
        return False
    return a == b
if __name__ == '__main__':
    print(equal(5, 5))
    print(equal(5, '5'))
    print(equal([1, 2], [1, 2]))
    print(equal([1, 2], [2, 1]))