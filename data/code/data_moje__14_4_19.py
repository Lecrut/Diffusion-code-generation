def fetch_third_item(items):
    if len(items) < 3:
        raise IndexError("List must contain at least three items")
    return items[2]

if __name__ == '__main__':
    sample_list = ["first", "second", "third", "fourth"]
    result = fetch_third_item(sample_list)
    print(result)