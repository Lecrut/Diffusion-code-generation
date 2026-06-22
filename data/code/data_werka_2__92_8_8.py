def bitwise_not_bool(value):
    return ~value & 1

if __name__ == '__main__':
    print(bitwise_not_bool(True))
    print(bitwise_not_bool(False))