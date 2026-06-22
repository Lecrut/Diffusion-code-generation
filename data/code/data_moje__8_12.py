import math

def scale_areas(shapes, factor=1.0):
    return [{"area": math.floor((s["width"] * s["height"]) * (factor ** 2))} for s in shapes]

if __name__ == '__main__':
    sample_shapes = [
        {"width": 10, "height": 20},
        {"width": 5, "height": 15},
        {"width": 8, "height": 8},
    ]
    result = scale_areas(sample_shapes, factor=2.0)
    print(result)