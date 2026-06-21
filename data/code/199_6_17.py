def longest_name(names):
    if not names:
        return None, 0

    def is_valid_name(name):
        return isinstance(name, str) and name.strip()

    valid_names = [name for name in names if is_valid_name(name)]
    
    if not valid_names:
        return None, 0

    longest = max(valid_names, key=len)
    length = len(longest)
    return longest, length

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Christopher", "Dave"]
    name, length = longest_name(sample_names)
    print(f"Longest Name: {name}, Length: {length}")