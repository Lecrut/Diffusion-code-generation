def box_surface_area(a, b, c):
    try:
        values = [a, b, c]
        for i, val in enumerate(values):
            if not isinstance(val, (int, float)):
                raise TypeError(f"Dimension {i} must be a number")
            if val <= 0:
                raise ValueError(f"Dimension {i} must be positive")
        return 2 * (a * b + b * c + c * a)
    except TypeError as e:
        raise e
    except ValueError as e:
        raise e

if __name__ == '__main__':
    print(box_surface_area(10, 20, 5))