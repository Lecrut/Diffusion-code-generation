def contains_value(target: int, iterable: Iterable[int]) -> bool:
    return target in iterable

if __name__ == '__main__':
    print(contains_value(3, [1, 2, 3, 4, 5]))