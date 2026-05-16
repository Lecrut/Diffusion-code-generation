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
    result_generator = fruit_color_generator(input_data)
    print("Processing fruit and color pairs:")
    for fruit, color in result_generator:
        print(f"Fruit: {fruit}, Color: {color}")