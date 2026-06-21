def get_third_item(items: list[str]) -> str:
    if len(items) < 3:
        raise IndexError("List must contain at least three items")
    return items[2]

if __name__ == '__main__':
    sample_list = ["first", "second", "third", "fourth"]
    result = get_third_item(sample_list)
    print(result)