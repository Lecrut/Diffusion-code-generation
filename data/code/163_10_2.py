fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple",
    "orange": "orange"
}

if __name__ == '__main__':
    for fruit, color in fruit_colors.items():
        print(f"{fruit.capitalize()} is {color}.")