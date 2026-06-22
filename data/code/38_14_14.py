def calculate_cone_volume(radius, height):
    return (1/3) * 3.141592653589793 * radius * radius * height

if __name__ == '__main__':
    radius = 5
    height = 10
    volume = calculate_cone_volume(radius, height)
    print(volume)