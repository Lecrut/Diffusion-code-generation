def validate_input(data):
    if not data:
        raise ValueError("Input list cannot be empty")

def find_max_value(items: list) -> float or int:
    validate_input(items)
    max_item = items[0]
    for item in items[1:]:
        if item > max_item:
            max_item = item
    return max_item

if __name__ == '__main__':
    sample_list = [3, 5.5, 1, 2, 4]
    print(find_max_value(sample_list))