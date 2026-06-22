import itertools

def chain_coordinates(triangle_coords, num_copies):
    return list(itertools.chain.from_iterable([triangle_coords] * num_copies))

if __name__ == '__main__':
    triangle_coords = [(0, 0), (1, 0), (0.5, 0.866)]
    num_copies = 3
    result = chain_coordinates(triangle_coords, num_copies)
    print(result)