import math

def scale_areas(shapes, factor=1):
    return [{"width": s["width"] * factor, "height": s["height"] * factor, "area": (s["width"] * factor) * (s["height"] * factor)} for s in shapes]

if __name__ == '__main__':
    sample_shapes = [
        {"width": 10, "height": 20},
        {"width": 5, "height": 15},
        {"width": 8, "height": 8}
    ]
    result = scale_areas(sample_shapes, 2)
    print(result)