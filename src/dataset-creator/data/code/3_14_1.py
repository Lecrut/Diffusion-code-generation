def parity(n: int) -> int:
    return (n & 1)
if __name__ == '__main__':
    print(parity(42))
    print(parity(43))