import numpy as np
def initialize_colormap(n_colors):
    return np.linspace(0, 1, n_colors)
def define_mapping(color_values, data_range):
    mapping = []
    for color in color_values:
        mapped_value = (color - color_values[0]) / (color_values[-1] - color_values[0])
        mapping.append(mapped_value)
    return np.array(mapping)
def test_colormap(color_map, sample_data):
    results = []
    for data in sample_data:
        mapped_result = []
        for i, color in enumerate(color_map):
            value = (data - sample_data[0]) / (sample_data[-1] - sample_data[0]) * (color + 1)
            mapped_result.append(value)
        results.append(np.array(mapped_result))
    return np.array(results)
if __name__ == '__main__':
    n_colors = 256
    color_map = initialize_colormap(n_colors)
    sample_data = np.linspace(0, 1, 10)
    test_results = test_colormap(color_map, sample_data)
    print(test_results)