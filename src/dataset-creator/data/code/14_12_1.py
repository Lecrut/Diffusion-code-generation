def create_presence_dict(item_names):
    presence_dict = {}
    for item in item_names:
        presence_dict[item] = True
    return presence_dict
if __name__ == '__main__':
    sample_items = ["apple", "banana", "apple", "orange", "banana", "apple"]
    result = create_presence_dict(sample_items)
    print(result)