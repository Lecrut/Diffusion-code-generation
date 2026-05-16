def favorite_color_generator():
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    for color in colors:
        yield color
if __name__ == '__main__':
    color_gen = favorite_color_generator()
    processed_colors = []
    for color in color_gen:
        processed_colors.append(color)
    print(processed_colors)