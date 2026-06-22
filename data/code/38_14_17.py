def calculate_cone_volume(radius, height):
    pi = 3.141592653589793
    return (1 / 3) * pi * radius * radius * height

if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    volume = calculate_cone_volume(radius, height)
    print(volume)