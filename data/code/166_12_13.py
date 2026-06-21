favorite_colors = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}

def get_hex_code(color_name):
    return favorite_colors.get(color_name, None)

if __name__ == '__main__':
    sample_color = 'purple'
    hex_code = get_hex_code(sample_color)
    if hex_code:
        print(f"The hex code for {sample_color} is {hex_code}")
    else:
        print(f"{sample_color} not found in the color dictionary.")