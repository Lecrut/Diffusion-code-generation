import itertools

def chain_triangle_coordinates(coords):
    if len(coords) != 4:
        raise ValueError("Coordinates must be a list of four integers")
    
    triangle_coords = [coords] * 3
    chained_coords = list(itertools.chain.from_iterable(triangle_coords))
    return chained_coords

if __name__ == '__main__':
    sample_coords = [1, 2, 3, 4]
    try:
        result = chain_triangle_coordinates(sample_coords)
        print(result)
    except ValueError as e:
        print(e)