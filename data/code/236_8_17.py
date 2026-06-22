def repeat_pattern(base_pattern: str, multiplier: int) -> str:
    return base_pattern * multiplier

if __name__ == '__main__':
    shape = "O"
    count = 20
    result = repeat_pattern(shape, count)
    print(result.strip())