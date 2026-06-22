def compute_trapezoid_area(bottom_base, top_base, altitude):
    total_base_length = bottom_base + top_base
    average_width = total_base_length / 2
    return average_width * altitude

if __name__ == '__main__':
    val_bottom = 12.5
    val_top = 8.5
    val_height = 6.0
    result = compute_trapezoid_area(val_bottom, val_top, val_height)
    print(result)