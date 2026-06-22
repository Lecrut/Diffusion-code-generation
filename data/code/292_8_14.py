PARALLELOGRAM_PERIMETER_CONSTANT = 2

def calculate_parallelogram_perimeter(base, height):
    return base * PARALLELOGRAM_PERIMETER_CONSTANT + height * PARALLELOGRAM_PERIMETER_CONSTANT

if __name__ == '__main__':
    parallelogram_base = 7
    parallelogram_height = 3
    perimeter = calculate_parallelogram_perimeter(parallelogram_base, parallelogram_height)
    print(f"Perimeter of parallelogram with base {parallelogram_base} and height {parallelogram_height}: {perimeter}")