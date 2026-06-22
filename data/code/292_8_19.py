def calculate_parallelogram_perimeter(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 2 * (base + height)

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    perimeter = calculate_parallelogram_perimeter(sample_base, sample_height)
    print(f"Perimeter of parallelogram with base {sample_base} and height {sample_height}: {perimeter}")