def calculate_box_properties(length, width, height, unit_cost):
    volume = length * width * height
    surface_area = 2 * (length * width + length * height + width * height)
    material_cost = surface_area * unit_cost
    return {
        "volume": volume,
        "surface_area": surface_area,
        "material_cost": material_cost
    }
if __name__ == '__main__':
    L = 10
    W = 5
    H = 2
    UC = 10.50
    properties = calculate_box_properties(L, W, H, UC)
    print(properties)