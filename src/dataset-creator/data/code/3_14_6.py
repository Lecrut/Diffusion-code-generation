def parity(n: int) -> int:
    return (n & 1) if n else 0
if __name__ == '__main__':
    print(parity(42))