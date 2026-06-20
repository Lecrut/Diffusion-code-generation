def compare_booleans(a, b):
    return (a == b, '==')

if __name__ == '__main__':
    print(compare_booleans(True, False))
    print(compare_booleans(False, False))