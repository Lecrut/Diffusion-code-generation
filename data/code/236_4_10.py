import itertools

def chain_triangle_coordinates(triangle_coords, num_copies):
    return list(itertools.chain.from_iterable(itertools.repeat(triangle_coords, num_copies)))

if __name__ == '__main__':
    triangle = [(0, 0), (1, 0), (0.5, 0.866)]
    copies = 3
    result = chain_triangle_coordinates(triangle, copies)
    print(result)