import math

PI_CONSTANT = math.pi

def compute_circle_area(r):
    if r < 0:
        raise ValueError("Radius must be non-negative")
    return PI_CONSTANT * (r * r)

if __name__ == '__main__':
    result_positive = compute_circle_area(7)
    print(result_positive)
    result_zero = compute_circle_area(0)
    print(result_zero)
    try:
        compute_circle_area(-5)
    except ValueError as error:
        print(str(error))