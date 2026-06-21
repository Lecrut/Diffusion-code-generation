def create_fruit_color_pairs():
    fruit_colors = {
        "apple": "red",
        "banana": "yellow",
        "cherry": "red",
        "date": "brown"
    }
    return list(fruit_colors.items())

if __name__ == '__main__':
    pairs = create_fruit_color_pairs()
    print(pairs)