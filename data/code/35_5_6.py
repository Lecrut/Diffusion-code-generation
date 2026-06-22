EDGE_PRESETS = {
    "tiny": 1.0,
    "small": 3.0,
    "medium": 5.0,
    "large": 10.0
}

def calculate_cube_volume(edge_length):
    return edge_length ** 3

if __name__ == '__main__':
    sample_edge = EDGE_PRESETS["medium"]
    volume = calculate_cube_volume(sample_edge)
    print(volume)