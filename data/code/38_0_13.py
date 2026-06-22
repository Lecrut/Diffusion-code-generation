def compute_cone_volume(radius, height):
    return (1.0 / 3.0) * 3.141592653589793 * radius ** 2 * height

if __name__ == '__main__':
    sample_radius = 5
    sample_height = 10
    result = compute_cone_volume(sample_radius, sample_height)
    print(result)