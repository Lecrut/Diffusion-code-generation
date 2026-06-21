from functools import reduce

def validate_input(data):
    if not data or not all(isinstance(item, str) for item in data):
        raise ValueError("Input must be a non-empty list of strings")

def find_longest_string(data):
    validate_input(data)
    return reduce(lambda x, y: x if len(x) > len(y) else y, data)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grape"]
    result = find_longest_string(sample_list)
    print(result)