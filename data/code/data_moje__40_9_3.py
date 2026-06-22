def calculate_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    dimensions = (1.5, 2.5, 3.5)
    result = calculate_surface_area(*dimensions)
    print(result)