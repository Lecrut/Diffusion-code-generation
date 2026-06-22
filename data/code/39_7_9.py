def prism_volume(base_area, height):
    if height <= 0 or base_area < 0:
        raise ValueError("Base area must be non-negative and height must be positive")
    return base_area * height

if __name__ == '__main__':
    result = prism_volume(10.0, 5.0)
    print(result)