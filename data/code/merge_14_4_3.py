def item_lengths(item_list):
    result = {}
    for item in item_list:
        result[item] = len(item)
    return result
if __name__ == '__main__':
    sample_items = ["apple", "banana", "kiwi", "orange", "grape"]
    lengths_dict = item_lengths(sample_items)
    print(lengths_dict)