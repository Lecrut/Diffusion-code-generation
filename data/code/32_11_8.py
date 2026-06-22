def area_for(shape, dimensions):
    shapes_map = {"rectangle": lambda w, h: w * h}
    area_fn = shapes_map[shape]
    return area_fn(*dimensions)

if __name__ == '__main__':
    result = area_for("rectangle", (8, 3))
    print(result)