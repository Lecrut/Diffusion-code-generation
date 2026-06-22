BASE_AREA = 50
HEIGHT = 10

def calculate_prism_volume(area, height):
    return area * height

if __name__ == '__main__':
    result = calculate_prism_volume(BASE_AREA, HEIGHT)
    print(result)