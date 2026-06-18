def check_zero(x):
    return x == 0 if isinstance(x, (int, float)) else False

if __name__ == '__main__':
    assert check_zero(0) is True
    assert check_zero(1) is False
    print("All tests passed.")