def process_items(sample_inputs):
    item_set = set()
    for item in sample_inputs:
        if item.lower() == 'done':
            break
        if isinstance(item, str) and item.strip():
            item_set.add(item.strip())
    return item_set
if __name__ == '__main__':
    sample_data = [
        "Apple",
        "Banana",
        "apple",
        "Orange",
        "done",
        123,
        "",
        "Grape",
        "Banana"
    ]
    result = process_items(sample_data)
    print(result)