def prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    base = 10.0
    h = 5.0
    result = prism_volume(base, h)
    print(result)