def scale_shape_areas(shapes, scale_factor):
    return [shape["width"] * shape["height"] * scale_factor for shape in shapes]

if __name__ == '__main__':
    shapes = [{"width": 2, "height": 3}, {"width": 5, "height": 4}, {"width": 1, "height": 1}]
    print(scale_shape_areas(shapes, 2))