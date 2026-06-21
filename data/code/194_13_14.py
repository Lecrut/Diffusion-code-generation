def validate_items(items):
    if not isinstance(items, list) or not all(isinstance(item, str) for item in items):
        raise ValueError("Input must be a list of strings")

def find_longest_item(items):
    validate_items(items)
    longest = max(items, key=len)
    return longest

if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry", "date"]
    print(find_longest_item(sample_items))