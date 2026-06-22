def prism_volume(base_area, height):
    if base_area < 0 or height < 0:
        return 0.0
    return base_area * height

if __name__ == '__main__':
    b = 8.5
    h = 3.0
    print(prism_volume(b, h))