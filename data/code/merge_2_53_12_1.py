def count_items_from_start(data: list) -> int:
    return len(list(filter(lambda x: isinstance(x, (int, float)), data)))
if __name__ == '__main__':
    sample_data = [10, "a", 20.5, None, True, False]
    result = count_items_from_start(sample_data)
    print(result)