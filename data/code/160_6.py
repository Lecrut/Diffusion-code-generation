if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry", "date"]
    item_dictionary = {}
    for item in sample_items:
        if item:
            item_dictionary[item] = True
    print(item_dictionary)