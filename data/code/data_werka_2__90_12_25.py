def check_or_condition(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Arguments must be boolean types")
    return bool(a | b)

if __name__ == '__main__':
    result = check_or_condition(True, False)
    print(result)