def create_item_list():
    try:
        items = ["Item 1", "Item 2", "Item 3"]
        return items
    except Exception as e:
        print(f"Error creating list: {e}")
        return []
if __name__ == '__main__':
    item_list = create_item_list()
    if not isinstance(item_list, list):
        raise TypeError("Expected a list but got an invalid type.")
    try:
        for index in range(len(item_list)):
            print(f"{index + 1}. {item_list[index]}")
    except IndexError as e:
        print(f"Error during display: {e}")