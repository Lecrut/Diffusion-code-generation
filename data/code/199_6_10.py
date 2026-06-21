MAX_NAME_LENGTH = 256

def longest_name(names):
    if not names:
        return None, 0
    longest = max(names, key=len)
    length = len(longest)
    return longest, length

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Christopher", "Dave"]
    name, length = longest_name(sample_names)
    print(f"Longest name: {name}, Length: {length}")