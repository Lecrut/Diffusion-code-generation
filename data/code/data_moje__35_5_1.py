EDGE_CATEGORIES = {
    "small": (0, 2),
    "medium": (2, 10),
    "large": (10, 100)
}

def get_edge_category(edge_length):
    for category, (lower, upper) in EDGE_CATEGORIES.items():
        if lower <= edge_length < upper:
            return category
    return "extra_large"

def calculate_cube_volume(edge_length):
    return edge_length * edge_length * edge_length

if __name__ == '__main__':
    sample_edge = 7
    volume = calculate_cube_volume(sample_edge)
    print(volume)