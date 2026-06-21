def create_fruit_color_pairs():
    fruit_color_data = {
        "apple": "red",
        "banana": "yellow",
        "cherry": "red",
        "date": "brown"
    }
    return list(fruit_color_data.items())

if __name__ == '__main__':
    pairs = create_fruit_color_pairs()
    print(pairs)