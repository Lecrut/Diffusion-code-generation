def count_items(collection):
    if isinstance(collection, dict):
        return len(collection)
    elif isinstance(collection, (list, tuple)):
        total = 0
        for item in collection:
            try:
                if not callable(item):
                    total += 1
            except Exception:
                pass
        return total
    else:
        raise TypeError("Unsupported collection type")
if __name__ == '__main__':
    sample_list = [1, 'a', None]
    empty_dict = {}
    sample_dict = {'x': 10, 'y': 20}
    result_list = count_items(sample_list)
    result_empty = count_items(empty_dict)
    result_dict = count_items(sample_dict)
    print(f"List items: {result_list}")
    print(f"Empty dict items: {result_empty}")
    print(f"Dict items: {result_dict}")