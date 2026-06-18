def build_item_list(items):
    if not isinstance(items, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    validated_items = []
    for idx, item in enumerate(items):
        try:
            str(item)                                                                                                                                                                            
            if not isinstance(item, (str, int)): 
                continue                                                                                                                                                                                         
            else:
                validated_items.append(str(item))
        except TypeError:
            raise ValueError(f"Element at index {idx} is not convertible to string.")
    return validated_items
if __name__ == '__main__':
    raw_data = ["Apple", 42, "Banana", None, [1, 2], True]
    try:
        final_list = build_item_list(raw_data)
        print("Validated Item List:", final_list)
    except (TypeError, ValueError) as e:
        print(f"Error encountered during list construction: {e}")