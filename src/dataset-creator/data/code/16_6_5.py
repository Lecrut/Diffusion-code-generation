def initialize_colormap(size):
    return [i / (size - 1) for i in range(size)]
def define_mapping(data, colormap):
    mapped_data = []
    for value in data:
        index = int((value - min(data)) / (max(data) - min(data)) * (len(colormap) - 1))
        mapped_value = colormap[index]
        mapped_data.append(mapped_value)
    return mapped_data
def test_colormap_mapping():
    sample_data = [10, 50, 90]
    colormap_size = 5
    colormap = initialize_colormap(colormap_size)
    print("Colormap:", colormap)
    results = define_mapping(sample_data, colormap)
    print("Sample Data:", sample_data)
    print("Mapped Results:", results)
if __name__ == '__main__':
    test_colormap_mapping()