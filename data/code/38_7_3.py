def calculate_cone_volume(radius, height):
    pi = 3.141592653589793
    return (1/3) * pi * radius * radius * height

if __name__ == '__main__':
    r = 7
    h = 5
    result = calculate_cone_volume(r, h)
    print(result)