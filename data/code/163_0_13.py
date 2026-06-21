fruit_colors = {
    'apple': 'red',
    'banana': 'yellow'
}

def get_fruit_color(fruit):
    try:
        return fruit_colors[fruit]
    except KeyError:
        raise ValueError(f"Invalid fruit: {fruit}")

if __name__ == '__main__':
    print(get_fruit_color('apple'))
    print(get_fruit_color('banana'))