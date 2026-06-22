def validate_input(a: int, b: int, c: int) -> bool:
    _MIN = 1
    _MAX = 100
    _MASK = 1

    def _is_valid(n: int) -> bool:
        return (_MIN < n < _MAX) and ((n & _MASK) == 0)

    return _is_valid(a) and _is_valid(b) and _is_valid(c)

if __name__ == '__main__':
    print(validate_input(2, 4, 6))
    print(validate_input(0, 4, 6))
    print(validate_input(2, 3, 6))
    print(validate_input(2, 4, 100))
    print(validate_input(-2, 4, 6))