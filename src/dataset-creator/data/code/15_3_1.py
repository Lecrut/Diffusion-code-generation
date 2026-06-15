def generate_predefined_list():
    items = [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry",
        "fig",
        "grape",
        "honeydew",
        "kiwi",
        "lemon"
    ]
    return tuple(items)
if __name__ == '__main__':
    result = generate_predefined_list()
    print(result)