import itertools

def chain_coordinates(coords):
    return list(itertools.chain.from_iterable(itertools.repeat(coords, 3)))

if __name__ == '__main__':
    sample_coords = [10, 20, 30, 40]
    repeated_coords = chain_coordinates(sample_coords)
    print(repeated_coords)