def contains(target: int, iterable: Iterable[int]) -> bool:
    return target in iterable

if __name__ == '__main__':
    print(contains(3, [1, 2, 3, 4, 5]))
    print(contains(6, range(10)))