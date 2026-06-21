class ColorDatabase:
    favorite_colors = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF', 'yellow': '#FFFF00', 'purple': '#800080', 'orange': '#FFA500', 'pink': '#FFC0CB', 'brown': '#964B00'}

    @staticmethod
    def get_hex_code(color_name):
        return ColorDatabase.favorite_colors.get(color_name, None)
if __name__ == '__main__':
    db = ColorDatabase()
    print(db.get_hex_code('red'))
    print(db.get_hex_code('green'))
    print(db.get_hex_code('blue'))
    print(db.get_hex_code('yellow'))
    print(db.get_hex_code('purple'))
    print(db.get_hex_code('orange'))
    print(db.get_hex_code('pink'))
    print(db.get_hex_code('brown'))
    print(db.get_hex_code('black'))