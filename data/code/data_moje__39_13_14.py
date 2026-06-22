BASE_AREA = 25
HEIGHT = 10

def calculate_prism_volume(area, height):
    return area * height

if __name__ == '__main__':
    volume = calculate_prism_volume(BASE_AREA, HEIGHT)
    print(volume)