import math

TWO = 2.0
PI = math.pi

def ellipse_area():
    MAJOR_AXIS = 8.0
    MINOR_AXIS = 4.0
    semi_major = MAJOR_AXIS / TWO
    semi_minor = MINOR_AXIS / TWO
    return PI * semi_major * semi_minor

if __name__ == '__main__':
    print(ellipse_area())