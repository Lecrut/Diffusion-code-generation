def create_item_list(items):
    try:
        return list(items) if isinstance(items, (list, tuple)) else []
    except TypeError as e:
        print(f"Error creating item list: {e}")
        return None
if __name__ == '__main__':
    sample_items = ["Apple", "Banana", "Cherry"]
    try:
        valid_input = create_item_list(sample_items)
        if valid_input is not None:
            print("Item List:")
            for index, item in enumerate(valid_input):
                print(f"{index + 1}. {item}")
            invalid_test = "Invalid Input"
            try:
                result = create_item_list(invalid_test)
            except Exception as e2:
                if isinstance(e2, TypeError):
                    print("Handled invalid input type correctly.")
        else:
            print("Failed to generate item list due to error.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")