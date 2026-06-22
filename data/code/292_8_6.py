def calculate_parallelogram_perimeter(base, height):
    return 2 * (base + height)

if __name__ == '__main__':
    base = 7
    height = 3
    perimeter = calculate_parallelogram_perimeter(base, height)
    print(f"Perimeter of parallelogram with base {base} and height {height}: {perimeter}")