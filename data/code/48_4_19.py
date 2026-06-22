def yield_largest():
    data = [10, 42, 7, 15, 99, 23, 56, 8, 31, 64]
    largest = None
    for point in data:
        if largest is None or point > largest:
            largest = point
        yield largest

if __name__ == '__main__':
    result = yield_largest()
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))