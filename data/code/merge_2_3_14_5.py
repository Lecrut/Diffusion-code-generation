def parity(n: int) -> int:
    return 1 if n & 1 else 0
if __name__ == '__main__':
    print(parity(42))
    print(parity(39))