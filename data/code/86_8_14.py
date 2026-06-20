if __name__ == '__main__':
    def compare_booleans(a: bool, b: bool) -> bool:
        return (a and not b) or (not a and b)

    x = True
    y = False
    assert isinstance(x, bool), f"Expected boolean type for x, got {type(x).__name__}"
    assert isinstance(y, bool), f"Expected boolean type for y, got {type(y).__name__}"
    result = compare_booleans(x, y)
    print(result)