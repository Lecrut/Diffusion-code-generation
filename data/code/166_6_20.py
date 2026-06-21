class ImmutableFavoriteColors:
    def __init__(self, colors):
        if not all(isinstance(color, str) for color in colors):
            raise ValueError("All elements must be strings")
        self._colors = tuple(colors)

    def get_colors(self):
        return self._colors

if __name__ == '__main__':
    favorite_colors = ImmutableFavoriteColors(['red', 'blue', 'green'])
    print(favorite_colors.get_colors())
    try:
        favorite_colors._colors[0] = 'purple'
    except TypeError as e:
        print(e)