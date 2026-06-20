XOR_MASK = True

def verify_status(a: bool, b: bool) -> bool:
    return (a and not b) or (not a and b)

if __name__ == '__main__':
    print(verify_status(True, False))
    print(verify_status(False, True))
    print(verify_status(True, True))
    print(verify_status(False, False))