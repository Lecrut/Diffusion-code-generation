def verify_status(a, b):
    return a ^ b
if __name__ == '__main__':
    print(verify_status(True, False))
    print(verify_status(False, True))
    print(verify_status(True, True))
    print(verify_status(False, False))