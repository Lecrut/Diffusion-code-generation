def extract_weights(data):
    """
    Recursively traverses a nested dictionary structure to extract all numerical weight values.
    
    Args:
        data (dict | list | float): The input data which can be a dictionary, 
                                    containing lists or floats as weights.
                                    
    Returns:
        list[float]: A flat list of all extracted numerical weight values.
    """
    weights = []

    def traverse(item):
        if isinstance(item, dict):
            for value in item.values():
                traverse(value)
        elif isinstance(item, (list, tuple)):
            for element in item:
                traverse(element)
        else:
            # Check if the item is a number (int or float) but not boolean
            if isinstance(item, (int, float)) and not isinstance(item, bool):
                weights.append(float(item))

    traverse(data)
    return weights

if __name__ == '__main__':
    pass
