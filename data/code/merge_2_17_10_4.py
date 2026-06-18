def check_item_in_list_or_dict(data):
    try:
        key = data[0]
        value = data[1]
        if isinstance(value, (list, tuple)):
            target = value[0]
            container = value[1]
            return any(item == target for item in container)
        elif isinstance(container, dict):
            return key in container
    except Exception:
        raise ValueError("Invalid input format. Expected (key_or_item, [container_type])")
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    target_in_list = "banana"
    sample_dict = {"a": 1, "b": 2, "c": 3}
    key_to_find = "b"
    result_list = check_item_in_list_or_dict([target_in_list, ["list", sample_list]])
    result_dict = check_item_in_list_or_dict([key_to_find, ["dict", sample_dict]])
    print(f"Item '{target_in_list}' found in list: {result_list}")
    print(f"Key '{key_to_find}' found in dict: {result_dict}")