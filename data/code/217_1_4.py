def is_strictly_greater(a: int, b: int) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError('Both inputs must be integers.')
    return a > b
if __name__ == '__main__':
    print(is_strictly_greater(5, 3))
    print(is_strictly_greater(2, 4))