def check_item_exists(stream, item):
    return any(x == item for x in stream)

if __name__ == '__main__':
    sample_stream = (i**2 for i in range(10))
    items_to_check = [3, 5, 8, 10]
    results = {item: check_item_exists(sample_stream, item) for item in items_to_check}
    print(results)