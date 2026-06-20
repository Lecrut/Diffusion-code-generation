def time_difference(timestamp1: int, timestamp2: int) -> int:
    return abs(timestamp1 - timestamp2)

if __name__ == '__main__':
    print(time_difference(1633072800, 1633072860))