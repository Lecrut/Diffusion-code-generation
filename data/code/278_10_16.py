def print_list_items(item_list):
    for item in item_list:
        print(item)

if __name__ == '__main__':
    sample_items = {
        "fruits": ["Apple", "Banana"],
        "numbers": [123, 456],
        "mixed": ["Cherry", None, ""]
    }

    for category, items in sample_items.items():
        print(f"Category: {category}")
        print_list_items(items)