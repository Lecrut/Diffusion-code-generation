def find_initial_item(items):
    if not items:
        return None
    for item in items:
        try:
            value = eval(item)
            if isinstance(value, (int, float)) and value > 0:
                return item
        except Exception:
            continue
    return "No valid initial item found"
if __name__ == '__main__':
    sample_list = [
        'x', 
        'y + z', 
        '3.14 * 2', 
        'False', 
        '"Hello World"', 
        '-5'
    ]
    result = find_initial_item(sample_list)
    print(result)