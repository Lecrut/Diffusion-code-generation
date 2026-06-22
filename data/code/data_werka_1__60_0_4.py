def fetch_last_item(collection):
    return collection[-1] if collection else None

if __name__ == '__main__':
    example_list = [5, 15, 25, 35, 45]
    last_item = fetch_last_item(example_list)
    print(last_item)