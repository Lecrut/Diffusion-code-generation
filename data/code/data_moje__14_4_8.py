def fetch_third_item(data: list[str]) -> str:
    if len(data) < 3:
        raise IndexError("List does not contain a third item")
    return data[2]

if __name__ == '__main__':
    items = ["first", "second", "third", "fourth"]
    result = fetch_third_item(items)
    print(result)