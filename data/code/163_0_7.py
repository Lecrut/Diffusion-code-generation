def fruit_colors():
    return {
        "apple": "red",
        "banana": "yellow"
    }

if __name__ == '__main__':
    colors = fruit_colors()
    print(f"Apple color: {colors['apple']}")
    print(f"Banana color: {colors['banana']}")