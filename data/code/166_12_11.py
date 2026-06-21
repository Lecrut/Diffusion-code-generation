class ColorDatabase:
    COLOR_MAP = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF', 'yellow': '#FFFF00', 'purple': '#800080', 'orange': '#FFA500', 'pink': '#FFC0CB', 'brown': '#A52A2A'}

    @staticmethod
    def get_hex_code(color_name):
        return ColorDatabase.COLOR_MAP.get(color_name, None)
if __name__ == '__main__':
    print(ColorDatabase.get_hex_code('red'))
    print(ColorDatabase.get_hex_code('green'))
    print(ColorDatabase.get_hex_code('blue'))
    print(ColorDatabase.get_hex_code('yellow'))
    print(ColorDatabase.get_hex_code('purple'))
    print(ColorDatabase.get_hex_code('orange'))
    print(ColorDatabase.get_hex_code('pink'))
    print(ColorDatabase.get_hex_code('brown'))
    print(ColorDatabase.get_hex_code('black'))