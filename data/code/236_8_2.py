def repeat_pattern(base_pattern: str, multiplier: int) -> str:
    return base_pattern * multiplier
if __name__ == '__main__':
    base = "abc"
    multiplier_val = 3
    result = repeat_pattern(base, multiplier_val)
    print(result)