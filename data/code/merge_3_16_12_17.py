def check_positive(x):
    return x > 0

if __name__ == '__main__':
    assert (check_positive(5) is True), "Test failed: positive number"
    assert (check_positive(-3) is False), "Test failed: negative number"
    assert (check_positive(0) is False), "Test failed: zero case"