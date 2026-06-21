def pair_fruit_with_color(fruits):
    fruit_colors = {
        "apple": "red",
        "banana": "yellow",
        "cherry": "red",
        "date": "brown",
        "elderberry": "purple"
    }
    return [(fruit, fruit_colors.get(fruit.lower(), "unknown")) for fruit in fruits]

if __name__ == '__main__':
    sample_fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig"]
    print(pair_fruit_with_color(sample_fruits))