def parallelogram_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Inputs must be numeric")
    if base <= 0 or height <= 0:
        raise ValueError("Inputs must be positive")
    return base * height

if __name__ == '__main__':
    result = parallelogram_area(5, 3)
    print(result)