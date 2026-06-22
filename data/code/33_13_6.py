def compute_triangle_area(base, height):
    def validate_dimensions(b, h):
        if b < 0 or h < 0:
            raise ValueError("Dimensions must be non-negative")
    validate_dimensions(base, height)
    return base * height * 0.5

if __name__ == '__main__':
    sample_base = 12
    sample_height = 8
    print(compute_triangle_area(sample_base, sample_height))