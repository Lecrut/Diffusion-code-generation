def negate_boolean(value):
    if value:
        return False
    return True

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))