def negate_boolean(value: bool) -> bool:
    return bool(value ^ 1)

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))