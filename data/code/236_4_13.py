import itertools

def repeat_triangle_coordinates(coords, count):
    return list(itertools.chain.from_iterable(itertools.repeat(coords, count)))

if __name__ == '__main__':
    sample_coords = [1, 2, 3, 4]
    repeated_coords = repeat_triangle_coordinates(sample_coords, 3)
    print(repeated_coords)