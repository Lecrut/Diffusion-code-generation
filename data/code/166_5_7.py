def count_favorite_colors():
    favorite_colors = ["red", "blue", "green", "yellow", "purple", "orange", "red", "green"]
    color_count = {}
    
    for color in favorite_colors:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    
    return color_count

if __name__ == '__main__':
    result = count_favorite_colors()
    print(result)