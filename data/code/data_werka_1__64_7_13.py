def find_all_indices(data, item):
    if not isinstance(data, list):
        raise ValueError("Data must be a list.")
    if not isinstance(item, (int, float, str)):
        raise ValueError("Item must be an int, float, or string.")
    
    for i, x in enumerate(data):
        if x == item:
            yield i

def find_final_index(data, item):
    try:
        generator = find_all_indices(data, item)
        last_index = None
        for index in generator:
            last_index = index
        return last_index
    except ValueError as e:
        print(f"Error: {e}")
        return -1

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60, 70]
    target_item = 40
    final_index = find_final_index(sample_data, target_item)
    print(final_index)