BASE_VALUE = 12.0
HEIGHT_VALUE = 6.0

def get_parallelogram_area(base: float, height: float) -> float:
    return base * height

if __name__ == '__main__':
    computed_area = get_parallelogram_area(BASE_VALUE, HEIGHT_VALUE)
    print(computed_area)