favorite_colors = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}

def get_color_hex(color_name):
    return favorite_colors.get(color_name, None)
if __name__ == '__main__':
    print(get_color_hex('red'))
    print(get_color_hex('yellow'))