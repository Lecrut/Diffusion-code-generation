def calculate_surface_area(dims):
    length = dims["length"]
    width = dims["width"]
    height = dims["height"]
    area_lw = length * width
    area_wh = width * height
    area_hl = height * length
    total = 2 * (area_lw + area_wh + area_hl)
    return total

if __name__ == '__main__':
    box_dimensions = {"length": 10, "width": 5, "height": 3}
    result = calculate_surface_area(box_dimensions)
    print(result)