def get_rectangular_box_surface_area(length: float, width: float, height: float) -> float:
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")
    area_lw = length * width
    area_wh = width * height
    area_hl = height * length
    total_area = 2 * (area_lw + area_wh + area_hl)
    return total_area

if __name__ == '__main__':
    dim_l = 7.5
    dim_w = 2.0
    dim_h = 3.0
    area_result = get_rectangular_box_surface_area(dim_l, dim_w, dim_h)
    print(area_result)