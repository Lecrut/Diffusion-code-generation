def contains_item(collection, item):
    return item in collection

if __name__ == '__main__':
    items = [10, 25, 33, 42, 56, 78, 91]
    target = 42
    if contains_item(items, target):
        print(f"The item {target} exists in the collection.")
    else:
        print(f"The item {target} does not exist in the collection.")