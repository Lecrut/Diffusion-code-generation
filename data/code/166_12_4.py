favorite_colors = {
    'red': '#FF0000',
    'green': '#00FF00',
    'blue': '#0000FF',
    'yellow': '#FFFF00',
    'purple': '#800080',
    'orange': '#FFA500',
    'pink': '#FFC0CB',
    'brown': '#964B00'
}

def get_hex_code(color_name):
    return favorite_colors.get(color_name, None)

if __name__ == '__main__':
    sample_color = 'purple'
    hex_code = get_hex_code(sample_color)
    print(f"The hex code for {sample_color} is: {hex_code}")