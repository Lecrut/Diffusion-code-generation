def calculate_parallelogram_perimeter(base, height):
    return 2 * (base + height)

if __name__ == '__main__':
    base_length = 6
    height_length = 4
    perimeter = calculate_parallelogram_perimeter(base_length, height_length)
    print(f"Perimeter of parallelogram with base {base_length} and height {height_length}: {perimeter}")