def compute_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    base_area = 15.0
    height = 20.0
    result = compute_prism_volume(base_area, height)
    print(result)