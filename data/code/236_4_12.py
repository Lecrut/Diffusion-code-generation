from itertools import repeat

def chain_triangle_coordinates(coords):
    return list(repeat(coords, 3))

if __name__ == '__main__':
    sample_coords = [1, 1, 5, 5]
    repeated_coords = chain_triangle_coordinates(sample_coords)
    print(repeated_coords)