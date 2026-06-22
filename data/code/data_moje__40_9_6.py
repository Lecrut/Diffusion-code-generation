def compute_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    dimensions = (1.5, 2.5, 3.5)
    result = compute_surface_area(*dimensions)
    print(result)