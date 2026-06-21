def validate_items(items):
    if not items:
        raise ValueError("The list of items cannot be empty")
    return items

def find_min_item(items):
    validated_items = validate_items(items)
    return min((item for item in validated_items))

if __name__ == '__main__':
    sample_items = [5, 3, 9, 1, 10]
    print(find_min_item(sample_items))