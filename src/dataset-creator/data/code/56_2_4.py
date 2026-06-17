def find_print_index(target_value):
    data = [10, 25, 30, 45, 60]
    for idx, val in enumerate(data):
        if val == target_value:
            return idx
    raise ValueError(f"Target value {target_value} not found.")
if __name__ == '__main__':
    try:
        result = find_print_index(45)
        print(result)
    except Exception as e:
        print(e)