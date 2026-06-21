favorite_colors = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF', 'yellow': '#FFFF00', 'purple': '#800080'}

def get_hex_code(color_name):
    return favorite_colors.get(color_name, None)
if __name__ == '__main__':
    print(get_hex_code('red'))
    print(get_hex_code('orange'))