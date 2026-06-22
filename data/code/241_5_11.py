def rectangle_area(length: float, width: float) -> float:
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return length * width

if __name__ == '__main__':
    try:
        area = rectangle_area(5.5, 3.2)
        print(f"Area: {area}")
    except ValueError as e:
        print(e)