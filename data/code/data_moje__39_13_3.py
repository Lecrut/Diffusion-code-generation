BASE_AREA = 10
HEIGHT = 5

def calculate_prism_volume(area, height):
    return area * height

if __name__ == '__main__':
    volume = calculate_prism_volume(BASE_AREA, HEIGHT)
    print(volume)