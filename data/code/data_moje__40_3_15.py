def surface_area(dimensions):
    x, y, z = dimensions
    return 2.0 * (x * y + x * z + y * z)

if __name__ == '__main__':
    dims = (3.0, 4.0, 5.0)
    result = surface_area(dims)
    print(result)