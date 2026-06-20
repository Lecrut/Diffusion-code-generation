def determine_outcome(a: int, b: int, c: int) -> bool:
    return (a & b) | (~c)

if __name__ == '__main__':
    print(determine_outcome(1, 2, 3))