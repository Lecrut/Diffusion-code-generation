def is_valid_string_list(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    for item in data:
        if not isinstance(item, str):
            raise TypeError("All items must be strings")

def find_minimum_lexicographically(data):
    is_valid_string_list(data)
    return min(data)

if __name__ == '__main__':
    sample_input = ["apple", "banana", "cherry"]
    try:
        minimum_value = find_minimum_lexicographically(sample_input)
        print(minimum_value)
    except Exception as e:
        print(e)