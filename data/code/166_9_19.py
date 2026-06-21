class FavoriteColors:
    DEFAULT_COLORS = {'red', 'blue', 'green', 'yellow', 'purple'}

    @staticmethod
    def is_color_favorite(color):
        return color in FavoriteColors.DEFAULT_COLORS
if __name__ == '__main__':
    print(FavoriteColors.is_color_favorite('red'))
    print(FavoriteColors.is_color_favorite('orange'))