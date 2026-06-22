def get_first_element(items):
    if not items:
        raise IndexError("Cannot get first element from an empty list")
    return items[0]

if __name__ == "__main__":
    sample_data = [10, 20, 30, 40, 50]
    print(get_first_element(sample_data))
    print(get_first_element(["apple", "banana", "cherry"]))
    print(get_first_element([{"key": "value"}]))