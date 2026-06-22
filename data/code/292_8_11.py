def calculate_parallelogram_perimeter(base, height):
    perimeter = 2 * (base + height)
    return perimeter

if __name__ == '__main__':
    sample_base = 7
    sample_height = 3
    parallelogram_perimeter = calculate_parallelogram_perimeter(sample_base, sample_height)
    print(f"Perimeter of parallelogram with base {sample_base} and height {sample_height}: {parallelogram_perimeter}")