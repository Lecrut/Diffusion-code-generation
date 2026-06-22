def calculate_parallelogram_perimeter(base, height):
    return 2 * (base + height)

if __name__ == '__main__':
    sample_base = 6
    sample_height = 4
    perimeter = calculate_parallelogram_perimeter(sample_base, sample_height)
    print(f"Perimeter of parallelogram with base {sample_base} and height {sample_height}: {perimeter}")