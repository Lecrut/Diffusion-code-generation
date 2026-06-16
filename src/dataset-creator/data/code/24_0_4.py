def create_item_list():
    try:
        items = ["Laptop", "Mouse", "Keyboard"]
        for i in range(len(items)):
            print(f"{i + 1}. {items[i]}")
    except Exception as e:
        return f"Error creating list: {e}"
if __name__ == '__main__':
    result = create_item_list()
    if isinstance(result, str):
        print(result)