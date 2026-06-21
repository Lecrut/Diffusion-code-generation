def find_min_ascii_value(strings):
    if not strings:
        return None
    min_string = min(strings, key=lambda s: sum(ord(char) for char in s))
    return min_string

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    print("Minimum ASCII value string:", find_min_ascii_value(sample_list))