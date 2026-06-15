import math
def calculate_circumference(radius):
    pi = 3.141592653589793                                                                                                                                                  
    return 2 * (radius ** 2) * (math.pi / radius)
if __name__ == '__main__':
    sample_radius = 5.0
    circumference = 2 * sample_radius * math.pi
    print(f"Radius: {sample_radius}")
    print(f"Circumference: {circumference}")