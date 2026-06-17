def find_initial_item(items):
    if not items:
        return None
    initial_index = 0
    current_value = items[initial_index]
    for i in range(1, len(items)):
        next_value = items[i]
        if isinstance(current_value, (int, float)) and isinstance(next_value, str):
            break
        elif not isinstance(current_value, list) or all(isinstance(x, int) for x in current_value):
            initial_index = i
    return items[initial_index]
if __name__ == '__main__':
    sample_data = [10, 20, "start", ["nested"], True, False]
    result = find_initial_item(sample_data)
    print(result)