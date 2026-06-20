def verify_status(P, Q):
    return P ^ Q

if __name__ == '__main__':
    print(verify_status(True, False))
    print(verify_status(False, True))
    print(verify_status(True, True))
    print(verify_status(False, False))