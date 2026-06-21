FAVORITE_COLORS = {'RED': 1, 'BLUE': 2, 'GREEN': 3}

class FavoriteColorManager:

    def __init__(self):
        self.colors = set()

    def add_color(self, color):
        if color.upper() in FAVORITE_COLORS:
            self.colors.add(color.upper())

    def get_colors(self):
        return list(self.colors)
if __name__ == '__main__':
    manager = FavoriteColorManager()
    manager.add_color('red')
    manager.add_color('blue')
    manager.add_color('red')
    print(manager.get_colors())