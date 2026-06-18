def initialize_colormap(size):
    return [i / (size - 1) for i in range(size)]
def define_mapping(data, colormap):
    mapped_data = []
    for value in data:
        index = int(value * (len(colormap) - 1))
        if index < len(colormap):
            mapped_value = colormap[index]
        else:
            mapped_value = colormap[-1]
        mapped_data.append(mapped_value)
    return mapped_data
def test_colormap_mapping():
    sample_data = [0.0, 0.5, 1.0, 2.5]
    colormap_size = 5
    colormap = initialize_colormap(colormap_size)
    print("Colormap:", colormap)
    result = define_mapping(sample_data, colormap)
    print("Sample Data:", sample_data)
    print("Mapped Results:", result)
if __name__ == '__main__':
    test_colormap_mapping()