import numpy as np
def initialize_colormap(n_colors):
    return np.linspace(0, 1, n_colors)
def define_mapping_logic(color_values, data_range):
    mapping = []
    for color in color_values:
        mapped_value = (color - color_values[0]) / (color_values[-1] - color_values[0]) * (data_range[1] - data_range[0]) + data_range[0]
        mapping.append(mapped_value)
    return np.array(mapping)
def test_colormap(color_map, sample_data):
    if len(color_map) != len(sample_data):
        raise ValueError("Color map size does not match sample data size")
    results = []
    for i in range(len(sample_data)):
        value = sample_data[i]
        index = np.digitize(value, color_map) - 1
        if index < 0:
            index = 0
        elif index >= len(color_map):
            index = len(color_map) - 1
        results.append(color_map[index])
    return np.array(results)
if __name__ == '__main__':
    N_COLORS = 5
    SAMPLE_DATA = np.array([0.1, 0.3, 0.5, 0.7, 0.9])
    DATA_RANGE = (0, 1)
    color_map = initialize_colormap(N_COLORS)
    print("Color Map:", color_map)
    mapping_logic = define_mapping_logic(color_map, DATA_RANGE)
    print("Mapping Logic:", mapping_logic)
    test_results = test_colormap(color_map, SAMPLE_DATA)
    print("Test Results:", test_results)