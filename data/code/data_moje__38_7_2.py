def calculate_cone_volume(radius, height):
    pi = 3.141592653589793
    return (1/3) * pi * (radius ** 2) * height

if __name__ == '__main__':
    radius = 7
    height = 5
    volume = calculate_cone_volume(radius, height)
    print(volume)