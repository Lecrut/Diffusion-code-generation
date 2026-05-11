if __name__ == '__main__':
    item_inputs = [
        "apple",
        "banana",
        "apple",
        "orange",
        "banana",
        "grape"
    ]
    item_dictionary = {}
    for item in item_inputs:
        item_dictionary[item] = True
    print(item_dictionary)