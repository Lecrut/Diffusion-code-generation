def find_min_ascii_value(strings):
    if not strings:
        return None
    current_min = strings[0]
    for s in strings[1:]:
        if s < current_min:
            current_min = s
    return current_min

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    min_value = find_min_ascii_value(sample_list)
    print("Minimum ASCII value string:", min_value)