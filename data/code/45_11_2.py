PI = 3.141592653589793
RADIUS = 5

def calculate_circle_area(radius):
    return PI * (radius ** 2)

if __name__ == '__main__':
    area = calculate_circle_area(RADIUS)
    print(area)