def calculate_cone_volume(radius, height):
    pi = 3.141592653589793
    volume = (1.0 / 3.0) * pi * radius * radius * height
    return volume

if __name__ == '__main__':
    result = calculate_cone_volume(7, 5)
    print(result)