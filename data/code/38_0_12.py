def compute_cone_volume(radius, height):
    return (1.0 / 3.0) * 3.141592653589793 * radius * radius * height

if __name__ == '__main__':
    radius = 3
    height = 5
    volume = compute_cone_volume(radius, height)
    print(volume)