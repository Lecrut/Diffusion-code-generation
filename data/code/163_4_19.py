fruit_color_pairs = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red",
    "date": "brown",
    "elderberry": "purple"
}

def filter_even_length_fruits(fruit_color_pairs):
    return {fruit: color for fruit, color in fruit_color_pairs.items() if len(fruit) % 2 == 0}

if __name__ == '__main__':
    filtered_pairs = filter_even_length_fruits(fruit_color_pairs)
    print(filtered_pairs)