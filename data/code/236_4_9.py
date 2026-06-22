import itertools

def repeat_triangle_coordinates(coords, count):
    triangle = list(itertools.repeat(coords, count))
    return triangle

if __name__ == '__main__':
    sample_coords = [1, 2, 3, 4]
    repeated_triangles = repeat_triangle_coordinates(sample_coords, 5)
    print(repeated_triangles)