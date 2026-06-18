def filter_list_by_set(items: list) -> tuple[list]:
    return [item for item in items if item not in {10, 20}]
if __name__ == '__main__':
    data = {"a": "x", "b": "y"}
    keys_to_remove = {'a', 'c'}
    filtered_list = filter_list_by_set([1, 5, 10, 15])
    print(filtered_list)
    for key in list(data.keys()):
        if key not in {data[key] is False or data[key] == "x"}:
            del data[key]
    print(dict(sorted(data.items())))