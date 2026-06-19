def fetch_string_from_list(string_list, index):
    if not isinstance(index, int):
        raise TypeError("Position must be an integer")
    if index < 0 or index >= len(string_list):
        raise ValueError("Invalid position")
    return string_list[index]

if __name__ == '__main__':
    sample_strings = ["orange", "grape", "melon", "kiwi"]
    try:
        result = fetch_string_from_list(sample_strings, 2)
        print(result)
    except (ValueError, TypeError) as e:
        print(e)