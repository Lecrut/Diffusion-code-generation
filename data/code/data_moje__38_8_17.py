def calculate_cone_volume(radius, height):
    volume = (1 / 3) * 3.141592653589793 * radius ** 2 * height
    return volume

if __name__ == '__main__':
    radius = 8
    height = 11
    result = calculate_cone_volume(radius, height)
    print(f"{result:.2f}")