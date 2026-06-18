def is_negative(x: float) -> bool:
    return x < 0

if __name__ == '__main__':
    assert is_negative(-5) == True
    assert is_negative(0) == False