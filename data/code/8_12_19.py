def scale_areas(shapes, scale_factor=1.0):
    return [{"width": s["width"], "height": s["height"], "area": s["width"] * s["height"] * scale_factor} for s in shapes]

if __name__ == '__main__':
    shapes = [
        {"width": 10, "height": 20},
        {"width": 5, "height": 15},
        {"width": 8, "height": 8}
    ]
    result = scale_areas(shapes, scale_factor=2.0)
    print(result)