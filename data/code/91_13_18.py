def negate_boolean(value: bool) -> bool:
    table = {True: 0, False: 1}
    inverted_int = table[value] ^ 1
    return bool(inverted_int)

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))