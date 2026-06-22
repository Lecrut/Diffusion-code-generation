def calculate_rhombus_area(d1, d2):
    if d1 < 0 or d2 < 0:
        raise ValueError("Diagonal lengths must be non-negative")
    if d1 == 0 or d2 == 0:
        return 0.0
    return 0.5 * d1 * d2

if __name__ == '__main__':
    sample_d1 = 6.0
    sample_d2 = 8.0
    result = calculate_rhombus_area(sample_d1, sample_d2)
    print(result)