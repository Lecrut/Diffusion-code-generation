def area_of_parallelogram(base, height):
    if not (isinstance(base, (int, float)) and isinstance(height, (int, float))):
        raise TypeError("Inputs must be numeric")
    if base <= 0 or height <= 0:
        raise ValueError("Inputs must be positive")
    return base * height

if __name__ == '__main__':
    result = area_of_parallelogram(10, 5)
    print(result)