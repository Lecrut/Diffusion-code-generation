def initialize_colormap(num_colors):
    return list(range(num_colors))
def define_mapping_logic(color_map, data):
    mapped_results = []
    for item in data:
        index = item % len(color_map)
        mapped_value = color_map[index] * 100
        mapped_results.append(mapped_value)
    return mapped_results
def test_colormap(sample_data):
    num_colors = 5
    color_map = initialize_colormap(num_colors)
    print("Color Map:", color_map)
    results = define_mapping_logic(color_map, sample_data)
    print("Sample Data:", sample_data)
    print("Mapped Results:", results)
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_colormap(sample_data)