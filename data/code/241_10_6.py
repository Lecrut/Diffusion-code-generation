WIDTH = 5.0
HEIGHT = 3.0

def calculate_area(width: float, height: float) -> float:
    return width * height

if __name__ == '__main__':
    area = calculate_area(WIDTH, HEIGHT)
    print(area)