def both_false(A: bool, B: bool) -> bool:
    return not A and not B

if __name__ == '__main__':
    x = False
    y = False
    result = both_false(x, y)
    print(result)