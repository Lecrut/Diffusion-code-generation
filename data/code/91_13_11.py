def negate_boolean(b):
    return bool(1 - int(b))

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))