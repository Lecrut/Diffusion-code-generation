def is_false(value: bool) -> bool:
    return not value

def both_false(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    return is_false(a) and is_false(b)

if __name__ == '__main__':
    x = False
    y = False
    result = both_false(x, y)
    print(result)