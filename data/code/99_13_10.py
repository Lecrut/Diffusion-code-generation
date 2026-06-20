def process_flags(a, b, c):
    return (a and b) or c

if __name__ == '__main__':
    print(process_flags(True, False, True))
    print(process_flags(False, False, False))
    print(process_flags(True, True, False))