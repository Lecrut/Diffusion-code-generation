def validate_dimensions(base, height):
    if base < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return base, height

def compute_triangle_area(base, height):
    validated_base, validated_height = validate_dimensions(base, height)
    return validated_base * validated_height / 2

if __name__ == '__main__':
    hardcoded_base = 12.0
    hardcoded_height = 8.0
    result = compute_triangle_area(hardcoded_base, hardcoded_height)
    print(result)