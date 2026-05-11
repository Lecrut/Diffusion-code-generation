def create_fruit_color_map(fruit_color_list):
    return {fruit: color for fruit, color in fruit_color_list}
if __name__ == '__main__':
    sample_data = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("grape", "purple"),
        ("orange", "orange"),
        ("strawberry", "red"),
        ("lemon", "yellow")
    ]
    color_map = create_fruit_color_map(sample_data)
    print(color_map)