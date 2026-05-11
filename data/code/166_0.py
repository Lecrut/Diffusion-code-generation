def store_favorite_colors():
    favorite_colors = {
        "red": "favorite",
        "blue": "favorite",
        "green": "favorite",
        "yellow": "favorite"
    }
    return favorite_colors
if __name__ == '__main__':
    colors = store_favorite_colors()
    print(colors)