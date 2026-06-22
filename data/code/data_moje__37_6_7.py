def parallelogram_area(base, height):
    if not (isinstance(base, (int, float)) and isinstance(height, (int, float))):
        raise TypeError("Base and height must be numeric")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive")
    return base * height

if __name__ == '__main__':
    result = parallelogram_area(5, 3)
    print(result)