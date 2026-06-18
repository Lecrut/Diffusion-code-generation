import numpy as np
def initialize_colormap(n_colors):
    return np.linspace(0, 1, n_colors)
def define_mapping_logic(color_map, data):
    mapped_values = np.zeros_like(data)
    for i in range(len(data)):
        mapped_values[i] = color_map[int(np.round(data[i] * (len(color_map) - 1)))]
    return mapped_values
def test_colormap(sample_data, num_colors):
    color_map = initialize_colormap(num_colors)
    result = define_mapping_logic(color_map, sample_data)
    return color_map, result
if __name__ == '__main__':
    sample_data = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    num_colors = 5
    color_map, mapped_result = test_colormap(sample_data, num_colors)
    print("Color Map:", color_map)
    print("Sample Data:", sample_data)
    print("Mapped Result:", mapped_result)