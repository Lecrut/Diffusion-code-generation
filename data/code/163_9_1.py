def main():
    fruit_colors = {
        "apple": "red",
        "banana": "yellow",
        "grape": "purple",
        "orange": "orange",
        "strawberry": "red"
    }
    for fruit, color in fruit_colors.items():
        print(f"{fruit}: {color}")
if __name__ == '__main__':
    main()