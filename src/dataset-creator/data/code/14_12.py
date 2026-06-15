def create_presence_dict(item_names):
    result = {}
    for item in item_names:
        result[item] = True
    return result
if __name__ == '__main__':
    sample_items = ["apple", "banana", "apple", "orange", "banana", "apple"]
    presence_dict = create_presence_dict(sample_items)
    print(presence_dict)