fruit_colors = {
    'apple': 'red',
    'banana': 'yellow'
}

def print_fruit_color(fruit):
    color = fruit_colors.get(fruit, "Unknown")
    print(f"{fruit}: {color}")

if __name__ == '__main__':
    print_fruit_color('apple')
    print_fruit_color('banana')
    print_fruit_color('cherry')