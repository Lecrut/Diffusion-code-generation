class ColorMapper:
    def __init__(self, color_map):
        self.color_map = color_map
    def map_colors(self, input_colors):
        mapped_result = {}
        for color in input_colors:
            if color in self.color_map:
                mapped_result[color] = self.color_map[color]
            else:
                mapped_result[color] = "Not Found"
        return mapped_result
if __name__ == '__main__':
    sample_colors = {
        "red": "crimson",
        "blue": "navy",
        "green": "emerald",
        "yellow": "gold"
    }
    mapper = ColorMapper(sample_colors)
    input_colors = ["red", "blue", "purple", "yellow"]
    result = mapper.map_colors(input_colors)
    print(result)