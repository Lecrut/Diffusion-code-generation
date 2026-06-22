def cube_volume(edge_length):
    return edge_length * edge_length * edge_length

if __name__ == '__main__':
    sample_edges = {
        "small": 3,
        "medium": 5,
        "large": 10.5
    }
    for label, edge in sample_edges.items():
        print(cube_volume(edge))