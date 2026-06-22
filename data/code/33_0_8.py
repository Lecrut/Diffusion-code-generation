def triangle_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numeric values.")
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    result = triangle_area(sample_base, sample_height)
    print(result)