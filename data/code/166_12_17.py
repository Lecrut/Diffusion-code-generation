favorite_colors = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}

def get_hex_code(color_name):
    return favorite_colors.get(color_name, None)

if __name__ == '__main__':
    color_to_query = "purple"
    hex_code = get_hex_code(color_to_query)
    print(f"The hex code for '{color_to_query}' is: {hex_code}")