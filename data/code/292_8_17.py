def calculate_parallelogram_perimeter(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 2 * (base + height)

if __name__ == '__main__':
    base = 7
    height = 3
    perimeter = calculate_parallelogram_perimeter(base, height)
    print(f"Perimeter of parallelogram with base {base} and height {height}: {perimeter}")