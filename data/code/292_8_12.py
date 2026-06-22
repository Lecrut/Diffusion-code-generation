def calculate_parallelogram_perimeter(base, height):
    return 2 * (base + height)

if __name__ == '__main__':
    parallelogram_base = 6
    parallelogram_height = 4
    perimeter = calculate_parallelogram_perimeter(parallelogram_base, parallelogram_height)
    print(f"Perimeter of parallelogram with base {parallelogram_base} and height {parallelogram_height}: {perimeter}")