def find_longest_item(mixed_list):
    string_items = [str(item) for item in mixed_list]
    longest_length = max(len(s) for s in string_items)
    longest_items = [s for s in string_items if len(s) == longest_length]
    return longest_items

if __name__ == '__main__':
    sample_data = ["apple", 123, "banana", {"key": "value"}, 4567890, "kiwi"]
    result = find_longest_item(sample_data)
    print(result)