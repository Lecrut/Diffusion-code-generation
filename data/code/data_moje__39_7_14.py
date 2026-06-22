def prism_volume(base_area, height):
    if base_area < 0:
        raise ValueError("Base area must be non-negative")
    if height < 0:
        raise ValueError("Height must be non-negative")
    return base_area * height

if __name__ == '__main__':
    base = 10.0
    h = 5.0
    result = prism_volume(base, h)
    print(result)