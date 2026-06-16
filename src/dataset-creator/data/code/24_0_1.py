def add_item(items: list[str], item_name: str) -> None:
    if not isinstance(item_name, str):
        raise TypeError("Item name must be a string.")
    items.append(item_name)
if __name__ == '__main__':
    shopping_list = []
    try:
        add_item(shopping_list, "Apple")
        add_item(shopping_list, "Banana")
        add_item(shopping_list, "Milk")
        for i, item in enumerate(shopping_list):
            print(f"{i + 1}. {item}")
    except Exception as e:
        print(f"An error occurred: {e}")