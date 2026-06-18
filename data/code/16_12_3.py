def is_positive(x: float) -> bool:
    return x > 0 if isinstance(x, (int, float)) else False

if __name__ == '__main__':
    assert is_positive(5) is True
    assert is_positive(-3) is False
    print("Tests passed.")