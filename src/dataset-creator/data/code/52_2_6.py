def get_last_item(data):
    if isinstance(data, list) and len(data) > 0:
        return get_last_item(data[-1])
    elif data is not None:
        return data
    else:
        raise ValueError("List structure contains no leaf items.")
if __name__ == '__main__':
    sample_data = [[[[[42]]], [3, 5]], "final_string", (6,), []]
    result = get_last_item(sample_data)
    print(result)