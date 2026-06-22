def repeat_pattern(base_pattern: str, multiplier: int) -> str:
    return base_pattern * multiplier

if __name__ == '__main__':
    pattern = "O"
    multiplier = 20
    result = repeat_pattern(pattern, multiplier)
    print(result)