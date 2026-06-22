BASE_SHAPE = "O"
MULTIPLIER = 20

def repeat_shape(base_pattern: str, multiplier: int) -> str:
    return base_pattern * multiplier

if __name__ == '__main__':
    result = repeat_shape(BASE_SHAPE, MULTIPLIER)
    print(result.strip())