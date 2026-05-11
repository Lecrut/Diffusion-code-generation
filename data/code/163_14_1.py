def fruit_color_generator(data):
    for fruit, color in data:
        yield fruit, color
if __name__ == '__main__':
    input_data = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("grape", "purple"),
        ("orange", "orange"),
        ("kiwi", "brown")
    ]
    fruit_color_pairs = fruit_color_generator(input_data)
    for fruit, color in fruit_color_pairs:
        print(f"Fruit: {fruit}, Color: {color}")