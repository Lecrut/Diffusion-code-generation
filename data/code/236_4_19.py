import itertools

def chain_triangle_coordinates(coords, times):
    return list(itertools.chain.from_iterable([coords] * times))

if __name__ == '__main__':
    sample_coords = [1, 1, 5, 5]
    repeated_coords = chain_triangle_coordinates(sample_coords, 3)
    print(repeated_coords)