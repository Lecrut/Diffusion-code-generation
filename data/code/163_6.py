def display_fruit_color_pairs(fruit_color_pairs):
    if not fruit_color_pairs:
        return
    max_fruit_len = max(len(fruit) for fruit, color in fruit_color_pairs)
    max_color_len = max(len(color) for fruit, color in fruit_color_pairs)
    for fruit, color in fruit_color_pairs:
        print(f"{fruit:<{max_fruit_len}} | {color:<{max_color_len}}")
if __name__ == '__main__':
    sample_data = [
        ("Apple", "Red"),
        ("Banana", "Yellow"),
        ("Grape", "Purple"),
        ("Orange", "Orange"),
        ("Strawberry", "Red"),
        ("Pineapple", "Yellow")
    ]
    display_fruit_color_pairs(sample_data)