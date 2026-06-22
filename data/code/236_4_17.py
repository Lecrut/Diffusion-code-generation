import itertools

TRIANGLE_COORDS = [(0, 0), (1, 1), (2, 0)]

def repeat_triangle(coords, times):
    return list(itertools.chain.from_iterable(itertools.repeat(coords, times)))

if __name__ == '__main__':
    repeated_coords = repeat_triangle(TRIANGLE_COORDS, 3)
    for coord in repeated_coords:
        print(f"{coord[0]}, {coord[1]}")