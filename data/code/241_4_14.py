WIDTH = 5
HEIGHT = 3

def calculate_area(width: int, height: int) -> int:
    return width * height

if __name__ == '__main__':
    area = calculate_area(WIDTH, HEIGHT)
    print(area)