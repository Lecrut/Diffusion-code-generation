def validate_item(item):
    return isinstance(item, str) and len(item.strip()) > 0
def construct_item_list(items):
    return [item for item in items if validate_item(item)]
if __name__ == '__main__':
    sample_data = ["apple", 123, "   ", None, "banana"]
    validated_list = construct_item_list(sample_data)