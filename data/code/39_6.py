def prism_volume(base_area, height):
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height must be non-negative")
    return base_area * height

if __name__ == '__main__':
    base = 50
    height_val = 12
    result = prism_volume(base, height_val)
    print(result)