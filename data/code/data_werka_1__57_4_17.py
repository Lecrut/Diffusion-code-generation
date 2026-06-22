def calculate_parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    base_length = 8
    height_length = 6
    area_result = calculate_parallelogram_area(base_length, height_length)
    print(f"Base: {base_length}")
    print(f"Height: {height_length}")
    print(f"Area of Parallelogram: {area_result}")