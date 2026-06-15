def generate_simple_list():
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
    result = generate_simple_list()
    print(result)