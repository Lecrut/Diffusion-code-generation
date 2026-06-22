def get_third_item(items: list[str]) -> str:
    if len(items) < 3:
        raise IndexError("List must contain at least three items")
    return items[2]

if __name__ == "__main__":
    sample_list: list[str] = ["first", "second", "third", "fourth", "fifth"]
    print(get_third_item(sample_list))