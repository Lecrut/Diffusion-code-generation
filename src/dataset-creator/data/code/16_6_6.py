import numpy as np
def initialize_colormap(n_colors):
    return np.linspace(0, 1, n_colors)
def define_mapping_logic(color_map, data):
    n_data = len(data)
    mapped_values = np.zeros(n_data)
    for i in range(n_data):
        index = int(np.round(data[i] * (len(color_map) - 1)))
        mapped_values[i] = color_map[index]
    return mapped_values
def test_colormap(sample_data, num_colors):
    color_map = initialize_colormap(num_colors)
    result = define_mapping_logic(color_map, sample_data)
    return result, color_map
if __name__ == '__main__':
    sample_data = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    num_colors = 8
    result, colormap = test_colormap(sample_data, num_colors)
    print("Sample Data:", sample_data)
    print("Color Map:", colormap)
    print("Mapped Results:", result)