def scale_areas(shapes, scale_factor=1.0):
    return [{"id": s.get("id"), "area": s.get("width", 1) * s.get("height", 1) * (scale_factor ** 2)} for s in shapes]

if __name__ == '__main__':
    shapes_list = [
        {"id": 1, "width": 10, "height": 5},
        {"id": 2, "width": 3, "height": 4},
        {"id": 3, "width": 7, "height": 2}
    ]
    result = scale_areas(shapes_list, 2.0)
    print(result)