def get_third_item(items: list) -> any:
    if not isinstance(items, list):
        raise TypeError("Input must be a list")
    if len(items) < 3:
        raise IndexError("List must contain at least three items")
    return items[2]

if __name__ == "__main__":
    sample_list = ["apple", "banana", "cherry", "date"]
    result = get_third_item(sample_list)
    print(result)