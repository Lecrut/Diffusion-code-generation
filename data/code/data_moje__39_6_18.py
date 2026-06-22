def compute_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    print(compute_prism_volume(10.0, 5.0))
    print(compute_prism_volume(3.14, 7.0))