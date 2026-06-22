import math
from decimal import Decimal, getcontext

getcontext().prec = 50

def calculate_ellipse_area_high_precision(major_axis: float, minor_axis: float) -> float:
    getcontext().prec = 50
    major = Decimal(str(major_axis))
    minor = Decimal(str(minor_axis))
    pi = Decimal(str(math.pi))
    area_decimal = pi * major * minor
    return float(area_decimal)

def calculate_ellipse_area_standard(major_axis: float, minor_axis: float) -> float:
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    test_major = 12.5
    test_minor = 8.3
    result_standard = calculate_ellipse_area_standard(test_major, test_minor)
    result_high_precision = calculate_ellipse_area_high_precision(test_major, test_minor)
    print(f"Standard Area: {result_standard}")
    print(f"High Precision Area: {result_high_precision}")