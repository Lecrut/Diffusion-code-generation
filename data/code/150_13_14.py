def validate_input(data, target):
    if not isinstance(data, list) or not all(isinstance(item, str) for item in data):
        raise ValueError("Data must be a list of strings")
    if not isinstance(target, str):
        raise ValueError("Target must be a string")

def filter_string_list(data, target):
    validate_input(data, target)
    return [item for item in data if item != target]

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "banana", "date"]
    target_to_filter = "banana"
    result = filter_string_list(sample_data, target_to_filter)
    print(result)