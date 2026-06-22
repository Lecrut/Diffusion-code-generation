def negate_boolean(value):
    return value ^ True

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))