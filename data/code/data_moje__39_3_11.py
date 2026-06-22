def prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    base = 10
    height = 5
    result = prism_volume(base, height)
    print(result)