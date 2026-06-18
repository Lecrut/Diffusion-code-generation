def get_last_item(data):
    if isinstance(data, list) and len(data) > 0:
        return get_last_item(data[-1])
    else:
        return data
if __name__ == '__main__':
    sample_data = [[[[[42]]], [3, [5]], "final"]]
    result = get_last_item(sample_data)
    print(result)