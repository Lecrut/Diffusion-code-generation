def get_third_item(data: list[str]) -> str:
    return data[2]

if __name__ == '__main__':
    items: list[str] = ["first", "second", "third", "fourth"]
    result: str = get_third_item(items)
    print(result)