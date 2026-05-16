if __name__ == '__main__':
    sample_items = [
        "apple",
        "banana",
        "apple",
        "orange",
        "banana",
        "grape"
    ]
    item_dictionary = {}
    for item in sample_items:
        item_dictionary[item] = True
    print(item_dictionary)