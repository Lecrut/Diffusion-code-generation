import math

def angle_conversion(degrees=None, radians=None, gradians=None):
    if degrees is not None:
        return (degrees * math.pi / 180), (degrees * 200 / 360)
    elif radians is not None:
        return (radians * 180 / math.pi), (radians * 200 / math.pi)
    elif gradians is not None:
        return (gradians * 90 / 200), (gradians * math.pi / 200)

if __name__ == '__main__':
    print(angle_conversion(degrees=180))
    print(angle_conversion(radians=math.pi))
    print(angle_conversion(gradians=200))