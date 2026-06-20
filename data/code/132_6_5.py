def verify_status(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    return a ^ b

if __name__ == '__main__':
    print(verify_status(True, False))
    print(verify_status(False, True))
    print(verify_status(True, True))
    print(verify_status(False, False))