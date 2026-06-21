class ColorMerger:
    def __init__(self):
        self.colors = set()

    def add_colors(self, color_list):
        self.colors.update(color_list)

    def get_unique_colors(self):
        return list(self.colors)

if __name__ == '__main__':
    merger = ColorMerger()
    colors1 = ["red", "blue", "green"]
    colors2 = ["blue", "yellow", "purple"]
    merger.add_colors(colors1)
    merger.add_colors(colors2)
    unique_colors = merger.get_unique_colors()
    print(unique_colors)