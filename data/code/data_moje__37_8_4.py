BASE = 7
HEIGHT = 4

def calculate_parallelogram_area(base, height):
    if base <= 0 or height <= 0:
        return 0
    return base * height

if __name__ == '__main__':
    result = calculate_parallelogram_area(BASE, HEIGHT)
    print(result)