fruit_colors = {
    'apple': 'red',
    'banana': 'yellow'
}

def print_fruit_color(fruit):
    if fruit in fruit_colors:
        color = fruit_colors[fruit]
        print(f"{fruit}: {color}")
    else:
        print(f"Unknown fruit: {fruit}")

if __name__ == '__main__':
    fruits_to_check = ["apple", "banana", "cherry"]
    for fruit in fruits_to_check:
        print_fruit_color(fruit)