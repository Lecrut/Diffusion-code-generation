fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red",
    "date": "brown",
    "elderberry": "purple"
}

def pair_fruit_with_color(fruits):
    return [(fruit, fruit_colors.get(fruit, "unknown")) for fruit in fruits]

if __name__ == '__main__':
    sample_fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    print(pair_fruit_with_color(sample_fruits))