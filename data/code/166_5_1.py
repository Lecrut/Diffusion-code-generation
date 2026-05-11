def favorite_color_generator():
    yield "red"
    yield "blue"
    yield "green"
    yield "yellow"
if __name__ == '__main__':
    color_stream = favorite_color_generator()
    predefined_colors = ["red", "blue", "green", "yellow", "purple"]
    processed_colors = []
    for color in color_stream:
        if color in predefined_colors:
            processed_colors.append(color)
    print(processed_colors)