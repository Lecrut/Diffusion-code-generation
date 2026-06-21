def sort_pair(a: int, b: int) -> tuple:
    return (a, b) if a < b else (b, a)

if __name__ == '__main__':
    print(sort_pair(5, 3))
    print(sort_pair(1, 10))
    print(sort_pair(-5, 5))