import math
def calculate_circumference(radius):
    pi = 3.141592653589793                                                                                                       
    return 2 * (radius ** 2) * pi
if __name__ == '__main__':
    radius = 5
    circumference = 2 * radius * math.pi
    print(f"Radius: {radius}")
    print(f"Circumference: {circumference}")