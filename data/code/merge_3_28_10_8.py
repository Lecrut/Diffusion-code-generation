def is_larger(a: float, b: float) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    assert (is_larger(5.0, 3.0)) == True
    assert (is_larger(2.1, 2.1)) == False
    assert (is_larger(-10.5, -9.8)) == False