def bitwise_and(a: int, b: int) -> bool:
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError('Both inputs must be integers')
    return a & 1 == 1 and b & 1 == 1
if __name__ == '__main__':
    print(bitwise_and(1, 1))
    print(bitwise_and(0, 1))
    print(bitwise_and(1, 0))
    print(bitwise_and(0, 0))