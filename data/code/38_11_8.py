def calculate_cone_volume(radius, height):
    pi = 3.141592653589793
    return (pi * radius * radius * height) / 3.0

if __name__ == '__main__':
    SAMPLE_RADIUS = 5.0
    SAMPLE_HEIGHT = 10.0
    result = calculate_cone_volume(SAMPLE_RADIUS, SAMPLE_HEIGHT)
    print(result)