favorite_colors = {
    'red': '#FF0000',
    'green': '#00FF00',
    'blue': '#0000FF',
    'yellow': '#FFFF00',
    'purple': '#800080'
}

def get_hex_code(color_name):
    return favorite_colors.get(color_name, None)

class ColorPalette:
    def __init__(self, color_dict=favorite_colors):
        self.colors = color_dict

    def fetch_color(self, color_name):
        return self.colors.get(color_name, None)

if __name__ == '__main__':
    palette = ColorPalette()
    print(palette.fetch_color('red'))
    print(palette.fetch_color('green'))
    print(palette.fetch_color('blue'))
    print(palette.fetch_color('yellow'))
    print(palette.fetch_color('purple'))