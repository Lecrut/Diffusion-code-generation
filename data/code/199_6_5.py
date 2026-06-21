def longest_name(names):
    if not names:
        return None, 0
    max_len = 0
    longest_name = ""
    for name in names:
        if len(name) > max_len:
            max_len = len(name)
            longest_name = name
    return longest_name, max_len

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Christopher", "Dave"]
    name, length = longest_name(sample_names)
    print(f"Longest Name: {name}, Length: {length}")