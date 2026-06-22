def calculate_box_surface_area(d1, d2, d3):
    area1 = d1 * d2
    area2 = d2 * d3
    area3 = d3 * d1
    return 2 * (area1 + area2 + area3)

if __name__ == '__main__':
    length = 4
    width = 6
    height = 8
    result = calculate_box_surface_area(length, width, height)
    print(result)