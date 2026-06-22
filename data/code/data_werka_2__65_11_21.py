def display_strings_with_indices(string_list):
    for position, text in enumerate(string_list):
        print(f"Position {position}: {text}")

if __name__ == '__main__':
    example_collection = ["grape", "honeydew", "kiwi", "lemon"]
    display_strings_with_indices(example_collection)