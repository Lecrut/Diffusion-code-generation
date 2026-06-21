class FavoriteColors:
    DEFAULT_COLORS = ["red", "blue", "green", "yellow", "purple"]

    @staticmethod
    def get_sorted_colors():
        return sorted(FavoriteColors.DEFAULT_COLORS)

if __name__ == '__main__':
    result = FavoriteColors.get_sorted_colors()
    print(result)