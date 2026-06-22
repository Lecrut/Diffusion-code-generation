def check_or_condition(a: bool, b: bool) -> bool:
    bits = {
        (0, 0): False,
        (0, 1): True,
        (1, 0): True,
        (1, 1): True,
    }
    return bits[(int(a), int(b))]

if __name__ == '__main__':
    result = check_or_condition(True, False)
    print(result)