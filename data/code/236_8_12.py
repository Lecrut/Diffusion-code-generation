SHAPE = "O"
MULTIPLIER = 20

def repeat_shape(shape: str, multiplier: int) -> str:
    return shape * multiplier

if __name__ == '__main__':
    result = repeat_shape(SHAPE, MULTIPLIER)
    print(result.strip())