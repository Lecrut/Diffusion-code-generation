def get_last_element(lst):
    slice_result = lst[-1:]
    return slice_result[0]

if __name__ == '__main__':
    category_map = {
        "fruit": ["apple", "banana", "cherry"],
        "vehicle": ["car", "truck", "motorcycle"],
        "planet": ["Earth", "Mars", "Venus"]
    }
    for category, items in category_map.items():
        print(get_last_element(items))