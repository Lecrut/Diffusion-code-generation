def is_strictly_positive(value: float) -> bool:
    return value > 0
if __name__ == '__main__':
    result = is_strictly_positive(5.7)
    print(result)
    assert not is_strictly_positive(-3.2), "Negative number test failed"