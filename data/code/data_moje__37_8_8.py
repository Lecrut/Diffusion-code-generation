def calculate_parallelogram_area(base, height):
    if base <= 0 or height <= 0:
        return 0
    return base * height

if __name__ == '__main__':
    print(calculate_parallelogram_area(7, 4))