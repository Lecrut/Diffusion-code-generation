def initialize_colormap(size):
    return [i / (size - 1) for i in range(size)]
def define_mapping_logic(data, colormap):
    mapped_data = []
    for value in data:
        index = int(value * (len(colormap) - 1))
        mapped_value = colormap[index]
        mapped_data.append(mapped_value)
    return mapped_data
def test_colormap_mapping(sample_data, colormap):
    results = define_mapping_logic(sample_data, colormap)
    return results
if __name__ == '__main__':
    SAMPLE_SIZE = 10
    COLORMAP = initialize_colormap(SAMPLE_SIZE)
    SAMPLE_DATA = [0.0, 0.25, 0.5, 0.75, 1.0]
    test_results = test_colormap_mapping(SAMPLE_DATA, COLORMAP)
    print("Colormap:", COLORMAP)
    print("Sample Data:", SAMPLE_DATA)
    print("Mapped Results:", test_results)