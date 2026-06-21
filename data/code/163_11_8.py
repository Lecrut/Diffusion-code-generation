def pair_fruits_with_colors(fruits):
    fruit_colors = {
        "apple": "red",
        "banana": "yellow",
        "cherry": "red",
        "date": "brown",
        "elderberry": "purple"
    }
    return [(fruit, fruit_colors.get(fruit, "unknown")) for fruit in fruits]

if __name__ == '__main__':
    sample_fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    print(pair_fruits_with_colors(sample_fruits))