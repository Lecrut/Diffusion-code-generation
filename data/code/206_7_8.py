def find_min_ascii_value(strings):
    if not strings:
        return None
    current_min = min(strings, key=lambda s: sum(ord(c) for c in s))
    return current_min

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    print("String with minimum ASCII value:", find_min_ascii_value(sample_list))