def calculate_parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    base = 8
    height = 3
    area = calculate_parallelogram_area(base, height)
    print(f"Base: {base}")
    print(f"Height: {height}")
    print(f"Area of parallelogram: {area}")