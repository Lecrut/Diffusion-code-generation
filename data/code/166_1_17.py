class ColorSorter:
    FAVORITE_COLORS = ["red", "blue", "green", "yellow"]

    @staticmethod
    def get_sorted_colors():
        return sorted(ColorSorter.FAVORITE_COLORS)

if __name__ == '__main__':
    result = ColorSorter.get_sorted_colors()
    print(result)