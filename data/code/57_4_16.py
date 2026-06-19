def calculate_parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    BASE = 10.0
    HEIGHT = 5.0
    area = calculate_parallelogram_area(BASE, HEIGHT)
    print(f"Base: {BASE}")
    print(f"Height: {HEIGHT}")
    print(f"Area of Parallelogram: {area}")